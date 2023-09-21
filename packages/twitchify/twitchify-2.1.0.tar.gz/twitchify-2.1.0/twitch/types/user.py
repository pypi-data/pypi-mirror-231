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

from typing import TypedDict, Literal, Optional


# ----------------------------
#       + Broadcaster +
# ----------------------------
class Broadcaster(TypedDict):
    broadcaster_id: str
    broadcaster_name: str
    broadcaster_login: str


class SpecificBroadcaster(TypedDict):
    broadcaster_user_id: str
    broadcaster_user_name: str
    broadcaster_user_login: str


class ToSpecificBroadcaster(TypedDict):
    to_broadcaster_user_id: str
    to_broadcaster_user_name: str
    to_broadcaster_user_login: str


class FromSpecificBroadcaster(TypedDict):
    from_broadcaster_user_id: str
    from_broadcaster_user_name: str
    from_broadcaster_user_login: str


# ----------------------------
#        + Moderator +
# ----------------------------
class Moderator(TypedDict):
    moderator_id: str
    moderator_name: str
    moderator_login: str


class SpecificModerator(TypedDict):
    moderator_user_id: str
    moderator_user_name: str
    moderator_user_login: str


# ---------------------------
#          + User +
# ---------------------------
class SpecificUser(TypedDict):
    user_id: str
    user_name: str
    user_login: str


class SpecificDisplayUser(TypedDict):
    user_id: str
    display_name: str
    user_login: str


class SpecificAnonymousUser(TypedDict):
    user_id: Optional[str]
    user_name: Optional[str]
    user_login: Optional[str]


UserType = Literal['admin', 'global_mod', 'staff', '']
BroadcasterType = Literal['affiliate', 'partner', '']
UserImages = TypedDict('UserImages', {'profile_image_url': str, 'offline_image_url': str})


class User(UserImages):
    id: str
    type: UserType
    email: str
    login: str
    created_at: str
    description: str
    display_name: str
    broadcaster_type: BroadcasterType


# -------------+ EventSub +-------------
class UserUpdateEvent(SpecificUser, total=False):
    email: str  # May sometimes be unavailable.
    description: str
    email_verified: bool
