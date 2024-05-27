from aiogram.types import BotCommand
from lexicon.lexicon import MENU_COMMANDS


async def set_main_menu(bot):
    main_menu_commands = [BotCommand(command=key, description=value)
                          for key, value in MENU_COMMANDS.items()]
    await bot.set_my_commands(main_menu_commands)
