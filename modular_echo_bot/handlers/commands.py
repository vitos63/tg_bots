from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardButton
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_RU
from handlers.keyboard_builder import create_keyboard,create_markups
from services.file_handling import book
from database import database
router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    database.users.add(message.from_user.id)
    database.bookmark[message.from_user.id]=set()
    await message.answer(text=LEXICON_RU['/start'])


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])


@router.message(Command(commands='beginning'))
async def process_beginning_command(message: Message):
    database.page_number[message.from_user.id] = 1
    await message.answer(text=book[1], reply_markup=create_keyboard(3, '<<', f'1/{max(book)}', '>>'))

@router.message(Command(commands='continue'))
async def process_beginning_command(message: Message):
    await message.answer(text=book[database.page_number[message.from_user.id]], reply_markup=create_keyboard(3, '<<', f'{database.page_number[message.from_user.id]}/{max(book)}', '>>'))

@router.message(Command(commands='bookmarks'))
async def process_beginning_command(message: Message):
    marks=create_markups(*database.bookmark[message.from_user.id])
    if marks:
        await message.answer(text='Это список ваших закладок', reply_markup= marks)
    else:
        await message.answer(text=LEXICON_RU['no_bookmarks'])



