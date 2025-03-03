from aiogram import Bot
from aiogram.types import BotCommand, InlineKeyboardButton, InlineKeyboardMarkup

from lexicon.lexicon import LEXICON

Ikb = InlineKeyboardButton

# клавиатура, для того чтобы начать читать или продолжить
def create_read_keyboard(*args):
    mini_il_kbd = InlineKeyboardMarkup(inline_keyboard=[
        [Ikb(text=LEXICON[key], callback_data=key) for key in args]
        ]
    )
    return mini_il_kbd
answer_il_kbd = InlineKeyboardMarkup(
    inline_keyboard=[[Ikb(text=LEXICON[button], callback_data=button)
                      for button in ['no', 'yes']]]
)


# главное меню
async def set_my_commands(bot: Bot):
    main_my_commands = [
        BotCommand(command='/start', description='Запуск'),
        BotCommand(command='/help', description='Справка')
    ]
    await bot.set_my_commands(main_my_commands)
