__title__ = 'tools_ai'
__author__ = 'nxSlayer'
__license__ = 'MIT'
__copyright__ = 'Copyright 2023 nxSlayer'

from .tools_ai import AI

from requests import get
from json import loads

__newest__ = loads(get("https://pypi.org/pypi/tools_ai/json").text)["info"]["version"]

if '1.1.0' != __newest__:
    print(f"(tools_AI) There is a new version, please update for better results")