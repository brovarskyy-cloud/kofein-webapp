import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import CommandStart

TOKEN = "8396253054:AAFIIuNREjRDbUspkY6CQC1J36nANWvZ7kA"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# старт
@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Привіт! Натисни кнопку, щоб відкрити меню 👇")

# отримання даних з WebApp
@dp.message()
async def handle_message(message: Message):
    if message.web_app_data:
        data = message.web_app_data.data
        await message.answer(f"🧾 Твоє замовлення:\n{data}")
    else:
        await message.answer("Я отримав твоє повідомлення 👍")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())