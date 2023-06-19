# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
<b> ❏ Commands for BOT Users
 ├ /start - Am i alive?
 ├ /about - About this Bot
 ├ /help - Need Help
 ├ /ping - To check live bot
 └ /uptime - To see bot status 
 
 ❏ Commands For BOT Admins
 ├ /logs - To view bot logs
 ├ /setvar - To set var with dibot command
 ├ /delvar - To remove var with command diabot
 ├ /getvar - To see one of the var with the command dibot
 ├ /users - To view bot user statistics
 ├ /batch - To link more than one file
 ├ /speedtest - To Test the bot server speed
 └ /broadcast - To send broadcast messages to bot users

👨‍💻 Develoved by </b><a href='https://t.me/DREAD_TOWER/4'>@Dread_Tower</a>
"""

    close = [
        [InlineKeyboardButton("Close", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            InlineKeyboardButton("Close", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("About Me", callback_data="about"),
            InlineKeyboardButton("Close", callback_data="close")
        ],
    ]

    ABOUT = """
<b>About this Bot:

@{} This is a Telegram Bot for storing posts or files that can be accessed via a special link.
 • Creator: @{}
 • Framework: <a href='https://docs.pyrogram.org'>Pyrogram</a>
 • Source Code: <a href='https://github.com/mrismanaziz/File-Sharing-Man'>File-Sharing-Man v4</a>

👨‍💻 Develoved by </b><a href='https://t.me/DREAD_TOWER/4</a>
"""
