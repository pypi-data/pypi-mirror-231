from aiogram import Bot, types


# Response for "start" command
async def response_start(msg: types.Message, bot: Bot):
    await msg.answer(f'Hello <b>{msg.from_user.first_name}</b>')
