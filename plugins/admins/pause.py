# Powered By @ashif903 & @mr_naveen720 
# Join @ODDRAGONS For More Updates
# Join @Ashif903 For Hacks
# Join Our Chats @ODDRAGONS & @mr_naveen720 


from pyrogram import filters
from pyrogram.types import Message

from Bikash.config import BANNED_USERS
from Bikash.Bgt import get_command
from Bikash import app
from Bikash.core.call import Bikashh
from Bikash.utils.database import is_music_playing, music_off
from Bikash.utils.decorators import AdminRightsCheck
from Bikash.utils.inline.play import close_keyboard

# Commands
PAUSE_COMMAND = get_command("PAUSE_COMMAND")


@app.on_message(
    filters.command(PAUSE_COMMAND)
    & filters.group
    & ~BANNED_USERS
)
@AdminRightsCheck
async def pause_admin(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    if not await is_music_playing(chat_id):
        return await message.reply_text(_["admin_1"])
    await music_off(chat_id)
    await Bikashh.pause_stream(chat_id)
    await message.reply_text(
        _["admin_2"].format(message.from_user.first_name),
        reply_markup=close_keyboard
    )


# Powered By @ashif903 & @mr_naveen720 
# Join @ODDRAGONS For More Updates
# Join @Ashif903 For Hacks
# Join Our Chats @ODDRAGONS & @mr_naveen720 
