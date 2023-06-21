import logging
from config import admins_id
from aiogram import Dispatcher


async def on_startup_notify(dp: Dispatcher):
    for admin in admins_id.split(","):
        try:
            text = "Bot launched successfully"
            if admin:
                await dp.bot.send_message(chat_id=int(admin), text=text)
        except Exception as e:
            logging.exception(e)
