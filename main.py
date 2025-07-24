import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.utils.token import TokenValidationError
from aiogram.client.default import DefaultBotProperties

API_TOKEN = os.getenv("7546832898:AAHa8iNE21MI2kiaEZ24Z_cQ0RhI7kxmAq4")

bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

@dp.message(F.text)
async def echo_handler(message: Message) -> None:
    await message.answer("Бот работает. Привет!")

async def main():
    logging.basicConfig(level=logging.INFO)
    try:
        await dp.start_polling(bot)
    except TokenValidationError:
        print("❌ Неверный API токен. Проверь переменную окружения API_TOKEN.")

if __name__ == "__main__":
    asyncio.run(main())