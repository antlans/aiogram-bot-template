from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from utils.misc import rate_limit


@rate_limit(5, 'help')
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = [
        'Список команд: ',
        '/start - Начать диалог',
        '/help - Получить справку',
        '/time - проверить текущее время',
        '/date - проверить текущую дату',
        '/geo - показать свою геопозицию',
        '/weather - погода в Хабаровске',
        '/currency - курс валюты',
        '/user_id - узнать свой ID',
    ]
    await message.answer('\n'.join(text))
