from aiogram import Router, F
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from lexicon.lexicon import LEXICON_RU, Turns
from random import choice
from handlers.yes_no import kb_builder
from handlers.commands import keybord
router = Router()


@router.message(F.text.in_(Turns))
async def make_a_move(message: Message):
    bot_move = choice(Turns)
    if message.text == bot_move:
        await message.answer(text=f'Мой выбор {bot_move}\nНичья!\nСыграем еще разок?', reply_markup=keybord)
    elif (bot_move == 'Камень' and message.text == 'Ножницы') or (bot_move == 'Бумага' and message.text == 'Камень') or (bot_move == 'Ножницы' and message.text == 'Бумага'):
        await message.answer(text=f'Мой выбор {bot_move}\nЯ победил!\nСыграем еще разок?', reply_markup=keybord)
    else:
        await message.answer(text=f'Мой выбор {bot_move}\nПоздравляю, ты выиграл!\nСыграем еще разок?', reply_markup=keybord)

@router.message()
async def other_message(message: Message):
    await message.answer(text=LEXICON_RU['other_message'])