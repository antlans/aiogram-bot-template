from aiogram import types

from filters import MyFilter

from loader import dp


@dp.message_handler(MyFilter(), regexp=r'(\d\d\d)')
async def bot_echo(message: types.Message):
    await message.answer('Я могу обрабатывать только числовые значения, как это: ' + message.text)
