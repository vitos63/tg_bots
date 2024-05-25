from aiogram import Router, F
from aiogram.types import Message, KeyboardButton, ReplyKeyboardRemove, ReplyKeyboardMarkup
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_RU

router = Router()
button_1 = KeyboardButton(text='Давай')
button_2 = KeyboardButton(text='Не хочу')
keybord = ReplyKeyboardMarkup(
    keyboard=[[button_1, button_2]], resize_keyboard=True, one_time_keyboard=True)


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=keybord)


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])
