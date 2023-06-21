from eternal.dispatcher import dp, bot
from aiogram import types
from eternal.config import PAY_TOKEN


@dp.message_handler(commands=["pay"])
async def payment(message: types.Message):
    await bot.send_invoice(
        message.chat.id,
        "Опрлата экскурсии",
        "Оплата экскурсии музей",
        payload="invoice",
        provider_token=PAY_TOKEN,
        currency="USD",
        prices=[types.LabeledPrice("Оплата экскурсии", 5 * 100)],
    )
