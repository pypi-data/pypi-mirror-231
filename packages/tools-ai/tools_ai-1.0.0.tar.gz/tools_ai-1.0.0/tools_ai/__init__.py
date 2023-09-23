__title__ = 'tools_ai'
__author__ = 'nxSlayer'
__license__ = 'MIT'
__copyright__ = 'Copyright 2023 nxSlayer'

from .socket import SocketDiscord
from .user_discord import ClientDiscord
from .utils import objects
from .utils import payloads
from .utils import Thread

from requests import get
from json import loads

__newest__ = loads(get("https://pypi.org/pypi/tools_ai/json").text)["info"]["version"]

if '1.0.0' != __newest__:
    print(f"(tools_AI) There is a new version, please update for better results")