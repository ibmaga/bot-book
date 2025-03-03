from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from keyboards import create_read_keyboard, answer_il_kbd
from database import database
from lexicon.lexicon import LEXICON

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, user_data):
    await message.answer(text=LEXICON['/start'], reply_markup=create_read_keyboard('read'))

    user_data[message.chat.id] = database.user_dict_template


@router.message(Command(commands=['help']))
async def cmd_help(message: Message):
    await message.answer(LEXICON['/help'], reply_markup=answer_il_kbd)
