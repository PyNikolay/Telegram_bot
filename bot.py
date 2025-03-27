from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command
import asyncio
from aiogram.utils.keyboard import InlineKeyboardBuilder

TOKEN = "7938866753:AAE0yEJP4bWfaUpQlNL7Z8Xr_GU7VtGVbcI"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: Message):
	keyboard = InlineKeyboardMarkup(
		inline_keyboard=[
			[InlineKeyboardButton(text="Channel", url="https://t.me/SIG_devs")]
		]
	)
	
	await message.answer("Hello! Join in our TG Channel @SIG_devs", reply_markup=keyboard)

async def main():
	print("Бот запущен")
	await bot.delete_webhook(drop_pending_updates=True)
	await dp.start_polling(bot)

if __name__ == "__main__":
	asyncio.run(main())
