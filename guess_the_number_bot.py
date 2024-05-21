from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from random import randint
bot_token = '7069583576:AAH0aQXr9L1e8pRw3ndPmc2r-zoJvYtQnNU'
bot = Bot(token=bot_token)
dp = Dispatcher()
user_settings = {'in_game': False, 'number': None,
                 'attemps': None, 'total_games': 0, 'wins': 0}
users = {}

attemps = 6
agree_answers = ['да', 'давай', 'согласен',
                 'конечно', 'сыграем', 'давай попробуем', 'играть', 'игра', 'хочу играть']
diagree_answers = ['нет', 'не хочу',
                   'в другой раз', 'откажусь', 'пожалуй откажусь']


def get_random_number():
    return randint(1, 100)


def add_user(user_id):
    users[user_id] = user_settings


async def start_command(message: Message):
    if message.from_user.id not in users[message.from_user.id]:
        add_user(message.from_user.id)
    await message.answer(f'Привет, {message.from_users[message.from_user.id].first_name}, сыграем в игру "Угадай число"?\nПодробные правила можешь прочитать по команде /help.\nСтатистику игр можно посмотреть по команде /stat.')


async def help_command(message: Message):
    if message.from_user.id not in users[message.from_user.id]:
        add_user(message.from_user.id)
    await message.answer(f'Я загадываю число от 1 до 100, у тебя есть {attemps} попыток, чтобы отгадать его, после каждой неудачной попытки я буду сообщать, больше загаданное число или меньше.')


async def cancel_command(message: Message):
    if users[message.from_user.id]['in_game']:
        users[message.from_user.id]['in_game'] = False
        await message.answer(f'Игра закончена\nЕсли хочешь сыграть снова - напиши')
    else:
        await message.answer(f'А мы и так не в игре, может сыграем разок?')


async def stat_command(message: Message):
    await message.answer(f'Всего игр сыграно: {users[message.from_user.id]["total_games"]}\nИгр выиграно: {users[message.from_user.id]["wins"]}')


async def agree_answer_command(message: Message):
    if message.from_user.id not in users[message.from_user.id]:
        add_user(message.from_user.id)
    if users[message.from_user.id]['in_game']:
        await message.answer('Мы и так в игре, напишите число или команду /cancel если хочешь выйти из игры')
    else:
        users[message.from_user.id]['in_game'] = True
        users[message.from_user.id]['number'] = get_random_number()
        users[message.from_user.id]['attemps'] = attemps
        await message.answer('Отлично, я загадал число, попробуй его отгадать')


async def disagree_answer_command(message: Message):
    if message.from_user.id not in users[message.from_user.id]:
        add_user(message.from_user.id)
    if users[message.from_user.id]['in_game']:
        await message.answer('Но мы уже в игре\nИспользуй команду /cancel если хочешь выйти из игры')
    else:
        await message.answer('Ну и пошел нахуй, хули ты тогда пришел сюда вообще?')


async def in_game_command(message: Message):
    if users[message.from_user.id]['in_game'] == False:
        await message.answer('Но мы еще не играем\nХотите сыграть?')
    elif users[message.from_user.id]['in_game']:
        if int(message.text) > users[message.from_user.id]['number']:
            users[message.from_user.id]['attemps'] -= 1
            await message.answer(f'Загаданное мной число меньше\nУ тебя осталось: {users[message.from_user.id]["attemps"]} попыток')
        elif int(message.text) < users[message.from_user.id]['number']:
            users[message.from_user.id]['attemps'] -= 1
            await message.answer(f'Загаданное мной число больше\nУ тебя осталось: {users[message.from_user.id]["attemps"]} попыток')
        elif int(message.text) == users[message.from_user.id]['number']:
            users[message.from_user.id]['total_games'] += 1
            users[message.from_user.id]['wins'] += 1
            users[message.from_user.id]['in_game'] = False
            await message.answer('Правильно, ты угадал число\nХочешь сыграть еще раз?')
        if users[message.from_user.id]['attemps'] <= 0:
            users[message.from_user.id]['in_game'] = False
            users[message.from_user.id]['total_games'] += 1
            await message.answer(f'Увы, но ты проиграл, повезет в следующий раз\nЗагаданное мной число было {users[message.from_user.id]["number"]}\nСыграем еще разок?')


async def another_message_command(message: Message):
    if message.from_user.id not in users[message.from_user.id]:
        add_user(message.from_user.id)
    if users[message.from_user.id][message.from_user.id]['in_game']:
        await message.answer('Пожалуйста, напишите целое число от 1 до 100 включительно')
    else:
        await message.answer('Я не понимаю, что вы написали\nВы хотите сыграть?')


dp.message.register(start_command, Command(commands=['start']))
dp.message.register(help_command, Command(commands=['help']))
dp.message.register(cancel_command, Command(commands=['cancel']))
dp.message.register(stat_command, Command(commands=['stat']))
dp.message.register(agree_answer_command, F.text.lower().in_(agree_answers))
dp.message.register(disagree_answer_command,
                    F.text.lower().in_(diagree_answers))
dp.message.register(
    in_game_command, lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 100)
dp.message.register(another_message_command)

if __name__ == '__main__':
    dp.run_polling(bot)
