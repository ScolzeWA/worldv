from typing import Union, List
from pyrogram import filters
from config import COMMAND_PREFIXES

COMMAND_YYYBD = None

other_filters = filters.group & ~ filters.edited & ~ filters.via_bot & ~ filters.forwarded
other_filters2 = filters.private & ~ filters.edited & ~ filters.via_bot & ~ filters.forwarded


def command(commands: Union[str, List[str]]):
    return filters.command(commands, COMMAND_PREFIXES)
    
def command2(commands: Union[str, List[str]]):
    return filters.command(commands, COMMAND_YYYBD)
