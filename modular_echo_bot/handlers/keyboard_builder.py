from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from lexicon.lexicon import LEXICON_RU
from services.file_handling import book

def create_keyboard(width: int, *args):
    kb_builder = InlineKeyboardBuilder()
    buttons = []
    for i in args:
        buttons.append(InlineKeyboardButton(
            text=LEXICON_RU[i] if i in LEXICON_RU else i, callback_data=i))
    kb_builder.row(*buttons, width=width)

    return kb_builder.as_markup()


def create_markups(*args):
    kb_builder = InlineKeyboardBuilder()
    if args:
        for i in sorted(args):
            kb_builder.row(InlineKeyboardButton(text=f'{i} - {book[i][:100]}', callback_data = str(i)))
    else:
        return 
    kb_builder.row(InlineKeyboardButton(text = LEXICON_RU['edit_bookmarks'], callback_data=LEXICON_RU['edit_bookmarks']),
                   InlineKeyboardButton(text = LEXICON_RU['cancel'], callback_data=LEXICON_RU['cancel']))
    return kb_builder.as_markup()


def edit_markups(*args):
    kb_builder = InlineKeyboardBuilder()
    if args:
        for i in sorted(args):
            kb_builder.row(InlineKeyboardButton(text=f'❌ {i} - {book[i][:100]}', callback_data = f'{i}del'))
    else:
        return 
    kb_builder.row(InlineKeyboardButton(text = LEXICON_RU['cancel'], callback_data=LEXICON_RU['cancel']))
    return kb_builder.as_markup()
