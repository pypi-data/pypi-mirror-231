"""
The MIT License (MIT)

Copyright (c) 2023-present Snifo

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""
from __future__ import annotations

from .errors import (WebSocketError, WebsocketClosed, NotFound, SessionClosed,
                     Forbidden, WebsocketUnused, WsReconnect)
from .utils import get_subscriptions
from json import JSONDecodeError
import asyncio
import aiohttp
import json

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Optional, List, Dict, Any, ClassVar
    from .types import http as HttpTypes
    from .state import ConnectionState

import logging
_logger = logging.getLogger(__name__)


__all__ = ('EventSubWebSocket',)


class EventSubWebSocket:
    """
    Represents EventSub WebSocket.
    """
    BASE: ClassVar[str] = 'wss://eventsub.wss.twitch.tv/ws'

    __slots__ = ('__connection', '__loop', 'subscriptions', '_keep_alive',
                 '_ws', '_ws_switch', 'session_id', 'cli')

    def __init__(self, *, connection: ConnectionState, loop: asyncio.AbstractEventLoop,
                 events: List[str]) -> None:
        self.__connection: ConnectionState = connection
        self.__loop: asyncio.AbstractEventLoop = loop
        self.subscriptions: List[HttpTypes.SubscriptionInfo] = get_subscriptions(events=events)
        # Default Session KeepAlive.
        self._keep_alive: int = 10
        self._ws: Optional[aiohttp.ClientWebSocketResponse] = None
        self._ws_switch: Optional[aiohttp.ClientWebSocketResponse] = None
        self.session_id: Optional[str] = None
        # Twitch CLI.
        self.cli: Optional[str] = None

    async def connect(self, reconnect: bool, url: str = BASE) -> None:
        """
        Connect to the WebSocket.
        """
        if self.cli:
            url = self.cli
        _retry = 0
        while True:
            _retry = (_retry % 6) + 1  # Cycle from 1 to 6 and back to 1
            try:
                _ws = await self.__connection.http.ws_connect(url=url)
                if self._ws is not None and not self._ws.closed:
                    self._ws_switch = self._ws
                    self._ws = _ws
                else:
                    self._ws = _ws
                await self.handle_messages()
            except WsReconnect as reconnect_url:
                url = str(reconnect_url)
                _logger.debug('Reconnecting to URL: %s', url)
                continue
            except (WebsocketClosed, SessionClosed, asyncio.TimeoutError) as error:
                if isinstance(error, WebsocketUnused):
                    raise
                if isinstance(error, SessionClosed):
                    _logger.error('Failed to establish a WebSocket connection due to a closed session. '
                                  'Retrying in %s seconds...', _retry * 5)
                else:
                    _logger.error('WebSocket connection failed: %s Retrying in %s seconds...',
                                  str(error), _retry * 5)
                await asyncio.sleep(5 * _retry)
            except (WebSocketError, aiohttp.ClientConnectorError) as error:
                if not self.__connection.http.is_force_closed:
                    if reconnect:
                        _logger.error('WebSocket connection error: %s Retrying in %s seconds...',
                                      str(error), _retry * 5)
                        await asyncio.sleep(5 * _retry)
                    else:
                        raise
                else:
                    raise

    async def handle_messages(self) -> None:
        """
        Handle incoming WebSocket messages.
        """
        while True:
            msg = await asyncio.wait_for(self._ws.receive(), timeout=(self._keep_alive + 10))
            if msg.type == aiohttp.WSMsgType.TEXT:
                await self.received_response(response=str(msg.data))
            elif msg.type == aiohttp.WSMsgType.CLOSED:
                _logger.error('WebSocket connection has been closed by the server.')
                close_code = self._ws.close_code
                if close_code == 4000:
                    raise WebsocketClosed(message='Internal server error.')
                elif close_code == 4001:
                    raise WebsocketClosed(message='Client sent inbound traffic.')
                elif close_code == 4003:
                    raise WebsocketUnused(message='Connection unused.')
                elif close_code == 4004:
                    raise WebsocketClosed(message='Reconnect grace time expired.')
                elif close_code == 4005:
                    raise WebsocketClosed(message='Network timeout.')
                elif close_code == 4006:
                    raise WebsocketClosed(message='Network error.')
                elif close_code == 4007:
                    raise WebsocketClosed(message='Invalid reconnect.')
                raise WebSocketError(message=f'Connection has been closed, Close code: {close_code}.')
            elif msg.type == aiohttp.WSMsgType.ERROR:
                exception = self._ws.exception()
                error_message = str(exception) if exception else 'Unknown error occurred.'
                raise WebSocketError(message=error_message)

    async def received_response(self, response: str) -> None:
        """
        Process the received response.
        """
        try:
            await self.__connection.socket_raw_receive(response)
            response: dict = json.loads(response)
        except (UnicodeDecodeError, JSONDecodeError) as error:
            _logger.error('Failed to parse response as JSON: %s. Response: %s', error, response)
            raise  # Re-raise the original error
        else:
            if response.get('metadata') is not None:
                metadata = response['metadata']
                # ====> Session Keepalive <====
                if metadata['message_type'] == 'session_keepalive':
                    _logger.debug('Received a keepalive message. The WebSocket connection is healthy.')
                # ====> Session Welcome <====
                elif metadata['message_type'] == 'session_welcome':
                    _session: HttpTypes.Session = response['payload']['session']
                    _logger.debug('Connected to WebSocket. Session ID: %s', _session['id'])
                    if self._ws_switch is None:
                        await self.__connection.connect()

                    # Close the old connection until the new reconnect websocket receive a
                    # Welcome message.
                    if self._ws_switch is not None and not self._ws_switch.closed:
                        await self.__connection.reconnect()
                        # Closing the old connection.
                        await self._ws_switch.close()
                        self._ws_switch = None
                    else:
                        # Subscribing to events.
                        subscribe = self.__connection.http.subscribe(
                            user_id=self.__connection.user.id,
                            session_id=_session['id'],
                            subscriptions=self.subscriptions)

                        self.__loop.create_task(subscribe, name='Twitchify:Subscriptions')
                    if _session['id'] != self.session_id:
                        if self.session_id is not None:
                            _logger.debug('A new WebSocket Session has been detected ID: %s', _session['id'])
                        self.session_id = _session['id']
                    # KeepAlive timeout.
                    self._keep_alive = _session['keepalive_timeout_seconds']

                # ====> Session Reconnect <====
                elif metadata['message_type'] == 'session_reconnect':
                    _session: HttpTypes.Session = response['payload']['session']
                    raise WsReconnect(url=_session['reconnect_url'])

                # ====> Subscription notification <====
                elif metadata['message_type'] == 'notification':
                    _subscription: HttpTypes.Subscription = response['payload']['subscription']
                    _event: Dict[Any] = response['payload']['event']
                    await self.__connection.parse(method=_subscription['type'], data=_event)

                # ====> Subscription Revocation <====
                elif metadata['message_type'] == 'revocation':
                    _subscription: HttpTypes.Subscription = response['payload']['subscription']
                    _status = _subscription['status']
                    # Revoked the authorization token that the subscription relied on.
                    if _status == 'authorization_revoked':
                        raise Forbidden(f'The user has revoked authorization for the'
                                        f' `{_subscription["type"]}` subscription.')
                    # The user mentioned in the subscription no longer exists.
                    elif _status == 'user_removed':
                        raise NotFound('The user mentioned in the subscription no longer exists.')
                    # Subscription type and version is no longer supported.
                    elif _status == 'version_removed':
                        _logger.warning('Subscription type `%s` version `%s` is no longer supported.',
                                        _subscription['type'], _subscription['version'])
