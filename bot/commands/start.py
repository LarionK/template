from aiogram import types
# from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton, KeyboardButtonPollType


async def start(message: types.Message) -> None:
    menu_builder = ReplyKeyboardBuilder()
    menu_builder.button(
        text='Помощь'
    )
    menu_builder.add(
        KeyboardButton(text='Отправить контакт', request_contact=True)
    )
    menu_builder.row(
        KeyboardButton(text='Отправить голосование', request_poll=KeyboardButtonPollType())
    )
    await message.answer(
        'Меню',
        reply_markup=menu_builder.as_markup(resize_keyboard=True)
        # reply_markup=ReplyKeyboardMarkup(keyword=menu_builder.export())

    )
