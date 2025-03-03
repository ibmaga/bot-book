from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

from lexicon.lexicon import LEXICON
from services import book

class CallFabric(CallbackData, prefix='del'):
    num: int

def create_bookmarks_kbd(bookmarks: set[int]) -> InlineKeyboardMarkup:
    bookmarks_kbd = InlineKeyboardBuilder()
    bookmarks_kbd.row(
        *[InlineKeyboardButton(
         text=f'{marks} - {book[marks][:100]}', callback_data=str(marks)) for marks in list(bookmarks)
        ],
        width=1
    )
    bookmarks_kbd.row(
        *[InlineKeyboardButton(text=LEXICON[i], callback_data=i)
          for i in ['cancel', 'edit_bookmarks_button']],
        width=1
    )

    return bookmarks_kbd.as_markup()


def del_bookmarks_kbd(bookmarks: set[int], del_index: int | None = None) -> InlineKeyboardMarkup:
    bookmarks_kbd = InlineKeyboardBuilder()

    if del_index is not None: # удаление выбранной закладки
        bookmarks.discard(del_index)
    bookmarks_kbd.row(
        *[InlineKeyboardButton(
            text=f'❌ {marks} - {book[marks][:100]}', callback_data=CallFabric(num=marks).pack()) for marks in list(bookmarks)
        ],
        width=1
    )
    bookmarks_kbd.row(
        InlineKeyboardButton(text=LEXICON['cancel'], callback_data='bookmarks'),
        width=1
    )

    return bookmarks_kbd.as_markup()
