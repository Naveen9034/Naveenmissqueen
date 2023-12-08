from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from Bikash import config
from Bikash import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥀 ❰ 𝐉𝐨𝐡𝐮𝐤𝐮𝐦 ❱ 💥",
                url=f"https://t.me/{BOT_USERNAME}?start=help",
            )
        ],
        [
            InlineKeyboardButton(
                text="⚙ 𝐁𝐨𝐭 𝐒𝐞𝐭𝐭𝐢𝐧𝐠 ⚙", callback_data="settings_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="💖 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 💖", url=f"https://t.me/ODDRAGONS"
            ),
            InlineKeyboardButton(
                text="💖 𝐆𝐫𝐨𝐮𝐩 💖", url=f"https://t.me/ODDRAGONS"
            )
        ],
        [           
            InlineKeyboardButton(
                text="📱 𝐆𝐫𝐨𝐮𝐩 📱", url=f"https://t.me/ODDRAGONS"
            )
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ ❰ 𝐉𝐚𝐧𝐚 𝐍𝐞𝐢𝐤𝐢 𝐉𝐚𝐨 ❱ ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="💖 𝐇𝐞𝐥𝐩 💖", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="🥀 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 💥", url=f"https://t.me/ODDRAGONS"
            ),
            InlineKeyboardButton(
                text="🥀 𝐆𝐫𝐨𝐮𝐩 💥", url=f"https://t.me/ODDRAGONS"
            )
        ],
        [           
            InlineKeyboardButton(
                text="📱 𝐆𝐫𝐨𝐮𝐩 📱", url=f"https://t.me/ODDRAGONS"
            )
        ],
        [
            InlineKeyboardButton(
                text="♕ 𝐁𝐚𝐚𝐩 ♕", user_id=OWNER
            )
        ]
     ]
    return buttons
