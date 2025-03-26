from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
import asyncio

TOKEN = "YOUR_TOKEN"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Hello! Join in our TG Channel @SIG_devs")

async def main():
	print("Бот запущен")
	await bot.delete_webhook(drop_pending_updates=True)
	await dp.start_polling(bot)

if __name__ == "__main__":
	asyncio.run(main())
