from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from lexicon.lexicon import LEXICON_RU
from database import database
from services.file_handling import book
from handlers.keyboard_builder import create_keyboard, edit_markups
from database.database import bookmark, page_number
router = Router()


@router.callback_query(F.data == '<<')
async def previous_page(callback: CallbackQuery):
    result = database.page_number[callback.from_user.id]
    if result > 1:
        database.page_number[callback.from_user.id] -= 1
        result -= 1
    await callback.message.edit_text(text=book[result], reply_markup=create_keyboard(3, '<<', f'{result}/{max(book)}', '>>'))


@router.callback_query(F.data == '>>')
async def next_page(callback: CallbackQuery):
    result = database.page_number[callback.from_user.id]
    if result < max(book):
        database.page_number[callback.from_user.id] += 1
        result += 1
    await callback.message.edit_text(text=book[result], reply_markup=create_keyboard(3, '<<', f'{result}/{max(book)}', '>>'))


@router.callback_query(lambda x: '/' in x.data and x.data.replace('/', '').isdigit())
async def add_mark_book(callback: CallbackQuery):
    bookmark[callback.from_user.id].add(
        database.page_number[callback.from_user.id])
    await callback.answer(LEXICON_RU['add_markup_text'])


@router.callback_query(F.data == LEXICON_RU['cancel'])
async def cancel_marks(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON_RU['cancel_text'])


@router.callback_query(F.data == LEXICON_RU['edit_bookmarks'])
async def edit_marks(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON_RU['edit_markup_text'], reply_markup=edit_markups(*bookmark[callback.from_user.id]))


@router.callback_query(lambda x: x.data.endswith('del') and x.data[:-3].isdigit())
async def del_marks(callback: CallbackQuery):
    bookmark[callback.from_user.id].remove(int(callback.data[:-3]))
    if bookmark[callback.from_user.id]:
        await callback.message.edit_text(text=LEXICON_RU['del_markup_text'], reply_markup=edit_markups(*bookmark[callback.from_user.id]))
    else:
        await callback.message.edit_text(text=LEXICON_RU['no_bookmarks'])


@router.callback_query(lambda x: x.data.isdigit())
async def go_to_mark_page(callback: CallbackQuery):
    text = book[int(callback.data)]
    page_number[callback.from_user.id] = int(callback.data)
    await callback.message.edit_text(text=text, reply_markup=create_keyboard(3, '<<', f'{callback.data}/{max(book)}', '>>'))


@router.message(lambda x: x.text.isdigit())
async def go_to_page(message: Message):
    text = book[int(message.text)]
    page_number[message.from_user.id] = int(message.text)
    await message.answer(text=text, reply_markup=create_keyboard(3, '<<', f'{message.text}/{max(book)}', '>>'))
