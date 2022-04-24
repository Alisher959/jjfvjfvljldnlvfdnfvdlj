from states.state_main import comment
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, CommandStart
from keyboards.default.first_keyboard import menu
from loader import dp, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    f = open('chat_id.txt', 'r')
    text = f.read()
    txt = text.split(',')
    have = 0
    for i in txt:
        if i == (f'{message.from_user.id}'):
            have = 1
        f.close()
    if have == 0:
        f = open('chat_id.txt', 'a')
        f.write(f'{message.from_user.id},')
        f.close()

    f = open('users.txt', 'r')
    text1 = f.read()
    txt1 = text1.split(',')
    have1 = 0
    print(txt1)
    for i in txt1:
        if i == f'{message.from_user.username}':
            have1 = 1
    f.close()
    if have1 == 0:
        f = open('users.txt', 'a')
        f.write(f'{message.from_user.username},')
        f.close()
    await message.answer(f"Hello, {message.from_user.full_name}!\n Welcome to my bot.", reply_markup=menu)


@dp.message_handler(text='💬 Leave a comment 💬')
async def send_comment(message: types.Message):
    await message.answer(f"💬 You can send comment about my portfolio.")
    await comment.comment_one.set()


@dp.message_handler(state=comment.comment_one)
async def comment_def(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=-1001166197867, text=f'@{message.from_user.username} dan fikr keldi\n{message.text}')
    await message.answer(f"Your comment is saved.")
    await state.finish()
