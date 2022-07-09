from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove


@dp.message_handler(commands=['start', 'help'])
async def commands_start(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, 'работает и спасибо', reply_markup=kb_client)
		await message.delete()
	except:
		await message.reply('общение черещ лс, обращайтесь по адресу:\n https://t.me/Lit_Range_bot')


def register_handlers_client(dp : Dispatcher):
	dp.register_message_handler(commands_start, commands=['start', 'help'])