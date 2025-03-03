from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery

class IsBookmarks(BaseFilter):
    async def __call__(self, query: CallbackQuery):
        if '/' in query.data:
            return {'num_page': int(query.data.split('/')[0])}
        return False

class IsInteger(BaseFilter):
    async def __call__(self, query: CallbackQuery):
        if query.data.isdigit():
            return {'num_page': int(query.data)}
        return False
