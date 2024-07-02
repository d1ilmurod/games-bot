from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


oyin_nomi = ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
oyin_nomi.add(
    KeyboardButton(text='Omad shou'),
)

oyin_tugmalari = ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
oyin_tugmalari.add(
    KeyboardButton(text="Aylantirish"),
    KeyboardButton(text="O'yindan Chiqish"),
)

javoblar = ReplyKeyboardMarkup(row_width=3,resize_keyboard=True)
javoblar.add(
    KeyboardButton(text="Ha albatta"),
    KeyboardButton(text="Yo'q rahmat"),
    KeyboardButton(text="Chiqish"),
)