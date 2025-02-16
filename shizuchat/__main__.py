import sys
import asyncio
import importlib
from flask import Flask
import threading
import config
from shizuchat import ID_CHATBOT
from pyrogram import idle
from pyrogram.types import BotCommand
from config import OWNER_ID
from shizuchat import LOGGER, shizuchat, userbot, load_clone_owners
from shizuchat.modules import ALL_MODULES
from shizuchat.modules.Clone import restart_bots
from shizuchat.modules.Id_chatbot import restart_idchatbots

async def anony_boot():
    try:
        await shizuchat.start()
        try:
            await shizuchat.send_message(int(OWNER_ID), f"**{shizuchat.mention} ɪꜱ ꜱᴛᴀʀᴛᴇᴅ❤️**")
        except Exception as ex:
            LOGGER.info(f"@{shizuchat.username} Started, please start the bot from owner id.")
    
        asyncio.create_task(restart_bots())
        asyncio.create_task(restart_idchatbots())
        await load_clone_owners()
        if config.STRING1:
            try:
                await userbot.start()
                try:
                    await shizuchat.send_message(int(OWNER_ID), f"ɪᴅ-ᴄʜᴀᴛʙᴏᴛ ᴀʟꜱᴏ ꜱᴛᴀʀᴛᴇᴅ 💕")
                except Exception as ex:
                    LOGGER.info(f"@{shizuchat.username} Started, please start the bot from owner id.")
    
            except Exception as ex:
                print(f"Error in starting id-chatbot :- {ex}")
                pass
    except Exception as ex:
        LOGGER.error(ex)

    for all_module in ALL_MODULES:
        importlib.import_module("shizuchat.modules." + all_module)
        LOGGER.info(f"Successfully imported : {all_module}")

    
    try:
        await shizuchat.set_bot_commands(
            commands=[
                BotCommand("start", "✧ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ✧"),
                BotCommand("help", "✧ ɢᴇᴛ ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ✧"),
                BotCommand("ping", "✧ ᴄʜᴇᴄᴋ ɪғ ᴛʜᴇ ʙᴏᴛ ɪs ᴀʟɪᴠᴇ ᴏʀ ᴅᴇsᴅ ✧"),
                BotCommand("shipping", "✧ ᴄᴏᴜᴘʟᴇs ᴏғ ᴅᴀʏ ✧"),
                BotCommand("rankings", "✧ ᴜsᴇʀ ᴍsɢ ʟᴇᴀᴅᴇʀʙᴏᴀʀᴅ ✧"),
            ]
        )
        LOGGER.info("Bot commands set successfully.")
    except Exception as ex:
        LOGGER.error(f"Failed to set bot commands: {ex}")
    
    LOGGER.info(f"@{shizuchat.username} Started.")
    
    await idle()


app = Flask(__name__)
@app.route('/')
def home():
    return "Bot is running"

def run_flask():
    app.run(host="0.0.0.0", port=8000)

if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()
    asyncio.get_event_loop().run_until_complete(anony_boot())
    LOGGER.info("Stopping Ronak Bot...")
