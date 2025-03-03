from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from lexicon.lexicon import LEXICON

def create_pagination(page, total_page):
    pagination_kbd = InlineKeyboardBuilder()
    if page == 1:
        pagination_kbd.row(
            *[InlineKeyboardButton(text=LEXICON['buttons'].get(button, button), callback_data=button)
              for button in [f'{page}/{total_page}', 'next', 'stop']],
            width=2
        )
    elif page == total_page:
        pagination_kbd.row(
            *[InlineKeyboardButton(text=LEXICON['buttons'].get(button, button), callback_data=button)
              for button in ['previous', f'{page}/{total_page}', 'stop']],
            width=2
        )
    else:
        pagination_kbd.row(
            *[InlineKeyboardButton(text=LEXICON['buttons'].get(button, button), callback_data=button)
              for button in ['previous',f'{page}/{total_page}', 'next', 'stop']],
            width=3
        )
    return pagination_kbd.as_markup()
