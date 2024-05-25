from aiogram import Router, F
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from lexicon.lexicon import LEXICON_RU
kb_builder = ReplyKeyboardBuilder()
buttons = [KeyboardButton(text=f'{i}')
           for i in ('Камень 🗿', 'Ножницы ✂', 'Бумага 📜')]
kb_builder.row(*buttons,width=1)
kb_builder : ReplyKeyboardMarkup = kb_builder.as_markup(resize_keyboard=True)
router = Router()


@router.message(F.text == 'Давай')
async def yes_answer(message: Message):
    await message.answer(text=LEXICON_RU['Давай'], reply_markup=kb_builder)


@router.message(F.text == 'Не хочу')
async def yes_answer(message: Message):
    await message.answer(text=LEXICON_RU['Не хочу'])
