from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
import asyncio

TOKEN = "YOUR_BOT_TOKEN"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: Message):
    await message.answer("Hello! Join in our TG Channel @SIG_devs")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(bot.delete_webhook())
    executor.start_polling(dp, skip_updates=True)
