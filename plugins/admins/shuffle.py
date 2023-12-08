
# Powered By @ashif903 & @mr_naveen720 
# Join @ODDRAGONS For More Updates
# Join @Ashif903 For Hacks
# Join Our Chats @ODDRAGONS & @mr_naveen720 

import random

from pyrogram import filters
from pyrogram.types import Message

from Bikash.config import BANNED_USERS
from Bikash.Bgt import get_command
from Bikash import app
from Bikash.misc import db
from Bikash.utils.decorators import AdminRightsCheck

# Commands
SHUFFLE_COMMAND = get_command("SHUFFLE_COMMAND")


@app.on_message(
    filters.command(SHUFFLE_COMMAND)
    & filters.group
    & ~BANNED_USERS
)
@AdminRightsCheck
async def admins(Client, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    check = db.get(chat_id)
    if not check:
        return await message.reply_text(_["admin_21"])
    try:
        popped = check.pop(0)
    except:
        return await message.reply_text(_["admin_22"])
    check = db.get(chat_id)
    if not check:
        check.insert(0, popped)
        return await message.reply_text(_["admin_22"])
    random.shuffle(check)
    check.insert(0, popped)
    await message.reply_text(
        _["admin_23"].format(message.from_user.first_name)
    )



# Powered By @ashif903 & @mr_naveen720 
# Join @ODDRAGONS For More Updates
# Join @Ashif903 For Hacks
# Join Our Chats @ODDRAGONS & @mr_naveen720 
