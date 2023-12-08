# Powered By @Mr_naveen720 @ASHIF903

from typing import Union, List
from pyrogram import filters
from Bikash.config import COMMAND_PREFIXES



def command(commands: Union[str, List[str]]):
    return filters.command(commands, COMMAND_PREFIXES)
