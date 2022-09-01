__all__ = ['reqister_user_commands']

from aiogram import Router
from aiogram.filters.command import CommandStart

from bot.commands.start import start


def reqister_user_commands(router: Router) -> None:
    # router.message.register(start, Command(commands=['start'], commands_prefix = ""))
    router.message.register(start, CommandStart)
