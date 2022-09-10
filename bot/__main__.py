import os
import asyncio
import logging
from aiogram import Dispatcher, Bot
from aiogram.types import BotCommand
from sqlalchemy.engine import URL

from commands import reqister_user_commands
from bot.commands.bot_commands import bot_commands

from db import BaseModel, create_async_engine, get_session_maker, proceed_schemas


async def main() -> None:
    logging.basicConfig(level=logging.DEBUG)

    commands_for_bot = []
    for cmd in bot_commands:
        commands_for_bot.append(BotCommand(command=cmd[0], description=cmd[1]))

    dp = Dispatcher()
    bot = Bot(token=os.getenv('token'))
    await bot.set_my_commands(commands=commands_for_bot)

    reqister_user_commands(dp)

    postgres_url = URL.create(
        "postgresql+asyncpg",
        username=
    )

    async_engine = create_async_engine(url=)
    session_marer = get_session_maker(async_engine)
    with session_marer() as session:
        proceed_schemas(session, BaseModel.metadata)

    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')
