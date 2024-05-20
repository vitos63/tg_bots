from aiogram import Bot, Dispatcher,F
from aiogram.filters import Command
from aiogram.types import Message
bot_token = '7069583576:AAH0aQXr9L1e8pRw3ndPmc2r-zoJvYtQnNU'
bot = Bot(token=bot_token)
dp = Dispatcher()

async def process_start_command(message: Message):
    await message.answer('Привет, я бот, который будет отвечать на твои сообщения таким же сообщением\nОтправь мне что-нибудь')


async def process_help_command(message: Message):
    await message.answer('Отправь мне сообщение и я отвечу на него таким же сообщением')


async def send_echo(message : Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text='Упс. неподходящий формат сообщения')


dp.message.register(process_start_command,Command(commands='start'))
dp.message.register(process_help_command,Command(commands='help'))
dp.message.register(send_echo)




if __name__ == '__main__':
    dp.run_polling(bot)
