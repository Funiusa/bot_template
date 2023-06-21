from eternal.dispatcher import dp
from aiogram import types


@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(
        types.KeyboardButton(
            "Open app",
            web_app=types.WebAppInfo(
            ),
        )
    )

    await message.reply("Hi!\nI'm bot.", reply_markup=kb)
