# Powered By @ashif903 & @mr_naveen720 
# Join @ODDRAGONS For More Updates
# Join @Ashif903 For Hacks
# Join Our Chats @ODDRAGONS & @mr_naveen720 



from typing import Union

from pyrogram import filters, types
from pyrogram.types import InlineKeyboardMarkup, Message

from Bikash import config
from Bikash.config import BANNED_USERS
from Bikash.Bgt import get_command, get_string, helpers
from Bikash import app
from Bikash.misc import SUDOERS
from Bikash.utils import help_pannel
from Bikash.utils.database import get_lang, is_commanddelete_on
from Bikash.utils.decorators.language import (LanguageStart,
                                                  languageCB)
from Bikash.utils.inline.help import (help_back_markup,
                                          private_help_panel)

### Command
HELP_COMMAND = get_command("HELP_COMMAND")


@app.on_message(
    filters.command(HELP_COMMAND)
    & filters.private
    & ~BANNED_USERS
)
@app.on_callback_query(
    filters.regex("settings_back_helper") & ~BANNED_USERS
)
async def helper_private(
    client: app, update: Union[types.Message, types.CallbackQuery]
):
    is_callback = isinstance(update, types.CallbackQuery)
    if is_callback:
        try:
            await update.answer()
        except:
            pass
        chat_id = update.message.chat.id
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = help_pannel(_, True)
        if update.message.photo:
            await update.edit_message_text(
                _["help_1"].format(config.SUPPORT_HEHE), reply_markup=keyboard
            )
        else:
            await update.edit_message_text(
                _["help_1"].format(config.SUPPORT_HEHE), reply_markup=keyboard
            )
    else:
        chat_id = update.chat.id
        if await is_commanddelete_on(update.chat.id):
            try:
                await update.delete()
            except:
                pass
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = help_pannel(_)
        await update.reply_photo(
            photo=config.START_IMG_URL,
            caption=_["help_1"].format(config.SUPPORT_HEHE), reply_markup=keyboard)


@app.on_message(
    filters.command(HELP_COMMAND)
    & filters.group
    & ~BANNED_USERS
)
@LanguageStart
async def help_com_group(client, message: Message, _):
    keyboard = private_help_panel(_)
    await message.reply_photo(
        photo=config.START_IMG_URL,
        caption=_["help_2"], reply_markup=InlineKeyboardMarkup(keyboard)
    )


@app.on_callback_query(filters.regex("help_callback") & ~BANNED_USERS)
@languageCB
async def helper_cb(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = help_back_markup(_)
    if cb == "hb9":
        if CallbackQuery.from_user.id not in SUDOERS:
            return await CallbackQuery.answer(
                "𝐓𝐡𝐢𝐬 𝐁𝐮𝐭𝐭𝐨𝐧 𝐈𝐬 𝐎𝐧𝐥𝐲 𝐅𝐨𝐫 𝐒𝐮𝐝𝐨 𝐔𝐬𝐞𝐫'𝐬.", show_alert=True
            )
        else:
            await CallbackQuery.edit_message_text(
                helpers.HELP_9, reply_markup=keyboard
            )
            return await CallbackQuery.answer()
    try:
        await CallbackQuery.answer()
    except:
        pass
    if cb == "hb1":
        await CallbackQuery.edit_message_text(
            helpers.HELP_1, reply_markup=keyboard
        )
    elif cb == "hb2":
        await CallbackQuery.edit_message_text(
            helpers.HELP_2, reply_markup=keyboard
        )
    elif cb == "hb3":
        await CallbackQuery.edit_message_text(
            helpers.HELP_3, reply_markup=keyboard
        )
    elif cb == "hb4":
        await CallbackQuery.edit_message_text(
            helpers.HELP_4, reply_markup=keyboard
        )
    elif cb == "hb5":
        await CallbackQuery.edit_message_text(
            helpers.HELP_5, reply_markup=keyboard
        )
    elif cb == "hb6":
        await CallbackQuery.edit_message_text(
            helpers.HELP_6, reply_markup=keyboard
        )
    elif cb == "hb7":
        await CallbackQuery.edit_message_text(
            helpers.HELP_7, reply_markup=keyboard
        )
    elif cb == "hb8":
        await CallbackQuery.edit_message_text(
            helpers.HELP_8, reply_markup=keyboard
        )
    elif cb == "hb10":
        await CallbackQuery.edit_message_text(
            helpers.HELP_10, reply_markup=keyboard
        )
    elif cb == "hb11":
        await CallbackQuery.edit_message_text(
            helpers.HELP_11, reply_markup=keyboard
        )
    elif cb == "hb12":
        await CallbackQuery.edit_message_text(
            helpers.HELP_12, reply_markup=keyboard
        )



# Powered By @ashif903 & @mr_naveen720 
# Join @ODDRAGONS For More Updates
# Join @Ashif903 For Hacks
# Join Our Chats @ODDRAGONS & @mr_naveen720 
