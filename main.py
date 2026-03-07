import asyncio
from aiogram import Bot,Dispatcher
from  aiogram.types import Message
from aiogram.filters import CommandStart

import os
from dotenv import load_dotenv
load_dotenv()



TOKEN = os.getenv("TOKEN")

bot= Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Hello there")

async def main():
    await dp.start_polling(bot)


print('hello')

if __name__ == '__main__':
    asyncio.run(main())



