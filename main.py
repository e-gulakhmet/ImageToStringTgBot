import asyncio
from os import getenv

import aiopytesseract
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message


TOKEN = getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("Token is not provided!")

bot = Bot(TOKEN)

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {message.from_user.full_name}!")


@dp.message()
async def message_handler(message: Message):
    if not message.photo:
        await message.answer("Please, send a photo!")
        return

    photo = message.photo[-1]
    file = await bot.download(photo)
    if not file:
        await message.answer("Failed to download the photo!")
        return

    image_text = await aiopytesseract.image_to_string(file.read())
    await message.answer(image_text)


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
