from keyboards.default.menu import menu
from aiogram import types
from aiogram import Bot,Dispatcher,executor
from loader import dp


@dp.message_handler(commands='menu')
async def menu_handler(message: types.Message):
    await message.answer("O'yinlarni tanlang",reply_markup=menu)