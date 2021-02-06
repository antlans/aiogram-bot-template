from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("help", "Получить помощь"),
        types.BotCommand("date", "Узнать дату"),
        types.BotCommand("time", "Узнать время"),
        types.BotCommand("weather", "Узнать погоду"),
        types.BotCommand("currency", "Узнать курс валюты"),
        types.BotCommand("user_id", "Узнать свой  телеграм ID"),
        types.BotCommand("user_form", "Заполнение своей анкеты")
    ])
