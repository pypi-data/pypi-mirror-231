from setuptools import setup
import re


def version() -> str:
    with open('twitch/__init__.py', encoding='utf-8') as file:
        text = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', file.read(),
                         re.MULTILINE).group(1)
        return text


def readme() -> str:
    with open('README.md', encoding='utf-8') as file:
        text = file.read()
        return text


setup(
    name='twitchify',
    version=version(),
    python_requires='>=3.8.0',
    packages=['twitch', 'twitch.bot', 'twitch.types'],
    author='Snifo',
    author_email='Snifo@mail.com',
    description='Real-time Twitch Event Handling and Helix API Integration in Python',

    url='https://github.com/mrsnifo/twitchify',
    project_urls={
            'Documentation': 'https://twitchify.readthedocs.io/en/latest',
            'Issue tracker': 'https://github.com/mrsnifo/twitchify/issues',
        },
    long_description=readme(),
    long_description_content_type='text/markdown',
    include_package_data=True,
    install_requires=['aiohttp>=3.8.0'],
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Typing :: Typed',
    ],
)
