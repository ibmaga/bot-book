from aiogram import Router, F
from aiogram.types import CallbackQuery

from lexicon.lexicon import LEXICON
from services import book
from keyboards import create_read_keyboard, create_pagination, create_bookmarks_kbd, del_bookmarks_kbd, CallFabric
from filters.for_handlers import IsBookmarks, IsInteger

router = Router()
total_page = len(book)


@router.callback_query(F.data.in_(['read', 'continue']))
async def read(callback: CallbackQuery, user_data: dict):
    page = user_data[callback.from_user.id]['page']
    await callback.message.edit_text(text=book[page], reply_markup= create_pagination(page, total_page))


@router.callback_query(F.data == 'next')
async def next_page(callback: CallbackQuery, user_data: dict):
    user_data[callback.from_user.id]['page'] += 1
    page = user_data[callback.from_user.id]['page']
    await callback.message.edit_text(text=book[page], reply_markup=create_pagination(page, total_page))


@router.callback_query(F.data == 'previous')
async def previous_page(callback: CallbackQuery, user_data: dict):
    user_data[callback.from_user.id]['page'] -= 1
    page = user_data[callback.from_user.id]['page']
    await callback.message.edit_text(text=book[page], reply_markup=create_pagination(page, total_page))


@router.callback_query(IsBookmarks())
async def save_value(callback: CallbackQuery, user_data: dict, num_page: int):
    user_data[callback.from_user.id]['bookmark'].add(num_page)
    await callback.answer(text=LEXICON['save_page'])


@router.callback_query(F.data.in_(['stop', 'cancel']))
async def stop(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON['stop'],
                                     reply_markup=create_read_keyboard('continue', 'bookmarks'))


@router.callback_query(F.data == 'bookmarks')
async def chose(callback: CallbackQuery, user_data: dict):
    await callback.message.edit_text(text=LEXICON['chose_bookmarks'],
                                     reply_markup=create_bookmarks_kbd(user_data[callback.from_user.id]['bookmark']))


@router.callback_query(F.data == 'edit_bookmarks_button')
async def edit_bookmarks(callback: CallbackQuery, user_data: dict):
    await callback.message.edit_text(text=LEXICON['edit_bookmarks'],
                                     reply_markup=del_bookmarks_kbd(user_data[callback.from_user.id]['bookmark']))


@router.callback_query(CallFabric.filter())
async def del_bookmarks(callback: CallbackQuery, callback_data: CallFabric, user_data: dict):
    user_data[callback.from_user.id]['bookmark'].discard(callback_data.num)
    await callback.message.edit_text(text=LEXICON['edit_bookmarks'],
                                     reply_markup=del_bookmarks_kbd(
                                         bookmarks=user_data[callback.from_user.id]['bookmark'],
                                         del_index=callback_data.num))


@router.callback_query(IsInteger())
async def del_bookmarks(callback: CallbackQuery, user_data: dict):
    page = int(callback.data)
    user_data[callback.from_user.id]['page'] = page
    await callback.message.edit_text(text=book[page], reply_markup=create_pagination(page, total_page))
