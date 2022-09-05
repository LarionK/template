from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.commands.callback_data_states import TestCallbackData


async def settings_command(message: types.Message):
    pass
    settings_markup = InlineKeyboardBuilder()
    settings_markup.button(
        text='Яндекс',
        url='yandex.ru'
    )
    settings_markup.button(
        text='Помощь',
        callback_data=TestCallbackData(text='Привет', user_id=message.from_user.id)
    )
    # await message.answer(f'{message.from_user.username}') username
    await message.answer('Настройки', reply_markup=settings_markup.as_markup())


async def settings_callback(call: types.CallbackQuery, callback_data: TestCallbackData):
    await call.message.answer(callback_data.text + ', ' + str(callback_data.user_id))

# async def call_help_func(call: types.CallbackQuery):
#     await call.message.edit_text(
#         'Эта кнопка редактирует сообщение с текстом в нужный текст'
#     ) но надо в регистре зарегистрировать router.callback_query.register(call_help_func, F.data == 'help')
#     reply_markup = call.message.reply_markup    если нужно передать клавиауру
