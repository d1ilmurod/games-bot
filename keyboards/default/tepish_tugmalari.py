from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


tepish = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="chap"),
            KeyboardButton(text="o'rta"),
            KeyboardButton(text="o'ng"),
        ],
        [
            KeyboardButton(text="ochkolar")
        ],

        [
            KeyboardButton(text="chiqish")
        ],
    ],
    resize_keyboard=True
)