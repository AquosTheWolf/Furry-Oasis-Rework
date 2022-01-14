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
    _member_remove_handlers: List[Callable[[discord.Member], None]] = []
    _reaction_add_handlers: List[Callable[[discord.Reaction, Union[discord.User, discord.Member]], None]] = []
    _reaction_remove_handlers: List[Callable[[discord.Reaction, Union[discord.User, discord.Member]], None]] = []

    _command_lookup: Dict[str, Callable[[discord.Message, str], None]] = {}

    _basic_help: Dict[str, str] = {}

    _long_help: Dict[str, Dict[str, str]] = {}

    unknown_command = "`Bad command or filename`\n(See bot help for help)"

    cmd_aliases: Dict[str, List[str]] = {}

    alias_lookup: Dict[str, str] = {}

    bot_name = config.bot_name