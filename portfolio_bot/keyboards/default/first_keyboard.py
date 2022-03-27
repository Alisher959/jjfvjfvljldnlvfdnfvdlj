from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💬 Leave a comment 💬"),
        ],
    ],
    resize_keyboard=True,
)