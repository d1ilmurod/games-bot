from aiogram import types
from aiogram import Bot,Dispatcher,executor
from loader import dp
from keyboards.default.tepish_tugmalari import tepish
from random import *
from keyboards.default.menu import menu

@dp.message_handler(text="Futbol game")
async def futbol_handler(message: types.Message):
    await message.answer("O'yin Hozir boshlanadi")
    await message.answer(f"{message.from_user.username} vs Other user")
    await message.answer("Qaysi tarafga tepasiz tugmalarda tanlang👇",reply_markup=tepish)

other_user = "Azamat"
other = 0
user = 0

# chap taraf uchun handler
@dp.message_handler(text='chap')
async def chap(message: types.Message):
    global other
    global user
    global other_user
    tanlash = message.text

    await message.answer('Siz chapga tepdingiz')
    tepish = ["o'ng", "o'rta", 'chap']
    tanladi = choice(tepish)


    if tanlash == tanladi:
        await message.answer("Zarbaaaa Goaaaal")
        user += 1
    else:
        await message.answer("Zarbaaaa")
        await message.answer(f"{other_user} {tanlash} ga otildi")
        await message.answer("To'pni ushladi")
        other += 1



@dp.message_handler(text="o'rta")
async def chap(message: types.Message):
    global other
    global user
    global other_user
    tanlash = message.text

    await message.answer("Siz o'rtaga tepdingiz")
    tepish = ["o'ng", "o'rta", 'chap']
    tanladi = choice(tepish)


    if tanlash == tanladi:
        await message.answer("Zarbaaaa Goaaaal")
        user += 1
    else:
        await message.answer("Zarbaaaa")
        await message.answer(f"{other_user} {tanlash} ga otildi")
        await message.answer("To'pni ushladi")
        other += 1


@dp.message_handler(text="o'ng")
async def chap(message: types.Message):
    global other
    global user
    global other_user
    tanlash = message.text

    await message.answer("Siz o'ng ga  tepdingiz")
    tepish = ["o'ng", "o'rta", 'chap']
    tanladi = choice(tepish)


    if tanlash == tanladi:
        await message.answer("Zarbaaaa Goaaaal")
        user += 1
    else:
        await message.answer("Zarbaaaa")
        await message.answer(f"{other_user} {tanlash} ga otildi")
        await message.answer("To'pni ushladi")
        other += 1

@dp.message_handler(text="ochkolar")
async def ochkolar(message: types.Message):
    global other_user
    if user > other:
        await message.answer(f"Ochko'lar\n{message.from_user.first_name} {user} : {other} Hisobi bilan g'olib bo'ldi")
    elif user < other:
        await message.answer(f"Ochko'lar\n{other_user} {other} : {user} Hisobu bilan g'olib bo'ldi")
    else:
        await message.answer(f"Ochko'lar\n{message.from_user.first_name} {user} : {other_user} {other}\nDurrang")




@dp.message_handler(text="chiqish")
async def chiqish(message: types.Message):
    await message.answer("Chiqish",reply_markup=menu)