from aiogram import types

# импортируем дефолтные пак фильтров из aiogram
from aiogram.dispatcher.filters import BoundFilter


class MyFilter(BoundFilter):

    async def check(self, message: types.Message):
        # если условие выполниться и функция вернет True, тогда фильтр выполниться
        # группы изменяем проверку на types.ChatType.GROUP
        return message.chat.type == types.ChatType.PRIVATE
