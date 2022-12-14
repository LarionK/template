__all__ = ['reqister_user_commands', 'bot_commands']

from aiogram import Router
from aiogram.filters.command import CommandStart, Command
from aiogram import F

from bot.commands.settings import settings_command, settings_callback
from bot.commands.start import start
from bot.commands.help import help_command, help_func, call_help_func
from bot.commands.callback_data_states import TestCallbackData
from bot.commands.bot_commands import bot_commands


def reqister_user_commands(router: Router) -> None:
    # router.message.register(start, Command(commands=['start']))
    router.message.register(start, CommandStart())
    router.message.register(help_command, Command(commands=['help', 'h']))
    router.message.register(settings_command, Command(commands=['settings']))
    router.message.register(start, F.text == "Старт")
    router.message.register(help_func, F.text == "Помощь")

    # router.callback_query.register(call_help_func, F.data == 'help')
    router.callback_query.register(settings_callback, TestCallbackData.filter())
