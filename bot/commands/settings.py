from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def settings_command(message: types.Message):
    pass
    settings_markup = InlineKeyboardBuilder()
    settings_markup.button(
        text='Яндекс',
        url='yandex.ru'
    )
    # settings_markup.button(
    #     text='Pay',
    #     pay=True
    # )
    await message.answer('Настройки', reply_markup=settings_markup.as_markup())
