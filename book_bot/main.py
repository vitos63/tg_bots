import asyncio
from aiogram import Bot, Dispatcher
from config_data.config import load_config
from keyboards.main_menu import set_main_menu
from handlers import commands, other_handlers
import logging


logger = logging.getLogger(__name__)

async def main():
    logging.basicConfig(
        level=logging.INFO, format='%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s')
    logging.info('Starting bot')

    config = load_config('.env')
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()
    await set_main_menu(bot)

    dp.include_routers(commands.router, other_handlers.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())
