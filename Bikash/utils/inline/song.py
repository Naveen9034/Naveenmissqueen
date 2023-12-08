from pyrogram.types import InlineKeyboardButton
from Bikash import config

def song_markup(_, vidid):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["SG_B_2"],
                callback_data=f"song_helper audio|{vidid}",
            ),
            InlineKeyboardButton(
                text=_["SG_B_3"],
                callback_data=f"song_helper video|{vidid}",
            ),
        ],
        [           
            InlineKeyboardButton(
                text="📱 𝐆𝐫𝐨𝐮𝐩 📱", url=f"url=f"https://t.me/ODDRAGONS""
            ),
        ],
        [
            InlineKeyboardButton(
                text="🥀 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 🥀", url=f"{https://t.me/ODDRAGONS}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data="close"
            ),
        ],
    ]
    return buttons
