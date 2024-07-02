from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Futbol game"),
            KeyboardButton(text="Omad shou"),
        ],
    ],
    resize_keyboard=True
)