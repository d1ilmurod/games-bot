from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.username}!")
    await message.answer("O'yinlar botiga xush kelibsiz")
    await message.answer("Botdagi o'yinlarni ko'rish uchun /menu bosing")
