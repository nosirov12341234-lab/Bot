import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

# Siz taqdim etgan token
TOKEN = "8492378780:AAHnlBLxficMcTsGq4bP0aQ80sEYFU2hXHs"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# /start bosilganda yoki xabar yozilganda "Salom" deydi
@dp.message()
async def send_salom(message: types.Message):
    await message.answer("Salom")

async def main():
    print("Bot ishlamoqda... To'xtatish uchun Ctrl+C bosing.")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot o'chirildi.")
