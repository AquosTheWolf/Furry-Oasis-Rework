from exceptions import UserBotError, HandlerError
from typing import List, Callable, Dict, Union

import asyncio
import config
import datetime
import discord
import log
import os
import prefix
import sys
import time
import traceback

class FrameworkClient(discord.Client):
    __version__ = "0.1"
    _background_tasks: List[Callable[[], None]] = []
    _ready_handlers: List[Callable[[], None]] = []
    _shutdown_handlers: List[Callable[[], None]] = []
    _message_handlers: List[Callable[[discord.Message], None]] = []
    _member_join_handlers: List[Callable[[discord.Member], None]] = []