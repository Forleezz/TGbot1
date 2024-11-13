import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from decouple import config

bot = Bot(token=config('TOKEN'))


dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.reply('Hello!!!')


@dp.message()
async def start_cmd(message: types.Message):
    await message.answer(message.text)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())
