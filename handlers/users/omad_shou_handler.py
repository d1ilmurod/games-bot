from aiogram import types
from aiogram import Bot,Dispatcher,executor
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InputFile
from loader import dp
from keyboards.default.omad_shou_tugmalari import oyin_tugmalari,javoblar,oyin_nomi
from random import *



baraban = [
    "30_000_000 so'm",
    "Damas",
    "40_000_000",
    "Nexia",
    "Iphone 15 pro max",
    "90_000_000 so'm",
    "60_000_000",
    "Gaz plita",
    "Telivizor",
    "Spark",
    "Malibu",
    "Ikki xonali uy",
    "Tracker",
    "50_000_000",
]



@dp.message_handler(text="Omad shou")
async def omad_shou(message: types.Message):
    await message.answer(f"Omad shou o'yiniga Xush kelibsiz {message.from_user.first_name}!")
    await message.answer(f"Hozir o'yin boshlanadi")
    await message.answer("barabandagi sovg'alar")
    rasim = InputFile(path_or_bytesio=(r"baraban_rasmi/baraban.jpg"))
    await message.bot.send_photo(chat_id=message.chat.id,photo=rasim)
    await message.answer("Barabanni aylantiring",reply_markup=oyin_tugmalari)

tanladi = choice(baraban)


@dp.message_handler(text="Aylantirish")
async def aylantirish(message: types.Message):
    await message.answer(f"Sizga {tanladi} tushdi olasizmi?",reply_markup=javoblar)


@dp.message_handler(text="Ha albatta")
async def ha(message: types.Message):
    if message.text == "Ha albatta":
        await message.answer(f"Tabriklayman siz {tanladi} sovg'ani yutdingiz",reply_markup=oyin_tugmalari)
    else:
        pass


@dp.message_handler(text="Yo'q rahmat")
async def yoq(message: types.Message):
    if message.text == "Yo'q rahmat":
        await message.answer(f"Marhamat o'yinni davom ettrishingiz mumkin",reply_markup=oyin_tugmalari)
        rasim = InputFile(path_or_bytesio=(r"baraban_rasmi/baraban.jpg"))
        await message.bot.send_photo(chat_id=message.chat.id, photo=rasim)
    else:
        pass


@dp.message_handler(text="Chiqish")
async def chiqish(message: types.Message):
    await message.answer(f"Chiqish",reply_markup=oyin_tugmalari)


@dp.message_handler(text="O'yindan Chiqish")
async def exit(message: types.Message):
    await message.answer("O'yindan chiqish",reply_markup=oyin_nomi)
