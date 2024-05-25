import asyncio
from aiogram import Bot, Dispatcher
from config_data.config import load_config
from handlers import other_handlers, yes_no, commands
import logging


logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO, format='%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s')
    logging.info('Starting bot')

    config = load_config('.env')
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    dp.include_routers(commands.router, yes_no.router, other_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())
