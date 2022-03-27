from states.state_main import comment
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command,CommandStart
from keyboards.default.first_keyboard import menu
from loader import dp,bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Hello, {message.from_user.full_name}!\n Welcome to my bot.", reply_markup=menu)

@dp.message_handler(text='💬 Leave a comment 💬')
async def bot_start(message: types.Message):
    await message.answer(f"💬 You can send comment about my portfolio.")
    await comment.comment_one.set()

@dp.message_handler(state=comment.comment_one)
async def bot_start(message: types.Message):
    await bot.send_message(chat_id=-1001166197867, text=f'@{message.from_user.username} dan fikr keldi\n{message.text}')
    await message.answer(f"Your comment is saved.")
    await comment.comment_one.finish()