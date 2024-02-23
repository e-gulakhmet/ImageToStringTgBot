import asyncio
from os import getenv

import aiopytesseract
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
import easyocr


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

    file_data = file.read()

    # Tesseract OCR
    tesseract_result = await aiopytesseract.image_to_string(file_data, lang="eng+rus")

    # EasyOCR
    easyocr_result = easyocr.Reader(["en", "ru"]).readtext(file_data, detail=0)
    easyocr_result = "\n".join(easyocr_result)

    result = f"Tesseract OCR:\n{tesseract_result}\n\nEasyOCR:\n{easyocr_result}"

    await message.answer(result)


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
