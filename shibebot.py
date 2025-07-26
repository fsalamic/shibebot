import logging
import requests
import json
import asyncio

from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters import Command
from aiogram.types import Message, URLInputFile

API_TOKEN = ''  # <-- Set your token here

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
router = Router()

# /start command
@router.message(Command("start"))
async def send_welcome(message: Message):
    await message.reply(
        "Hi!\nI'm ShibeBot by @fsalamic!\nPowered by aiogram v3.\nSource Code: https://github.com/fsalamic/shibebot"
    )

# /help command
@router.message(Command("help"))
async def send_help(message: Message):
    await message.reply(
        "To use this bot do:\n"
        " /shiba - if you want a shibe picture\n"
        " /cat - if you want a cat picture\n"
        " /dog - if you want a bird picture."
    )

# /shiba command
@router.message(Command("shiba"))
async def send_shiba(message: Message):
    url = "https://api.thedogapi.com/v1/images/search?breed_ids=222&limit=1&api_key="
    r = requests.get(url)
    data = r.json()
    shiba_url = data[0]["url"]
    image = URLInputFile(shiba_url, filename="shiba.jpg")
    await bot.send_photo(message.chat.id, image)

# /dog command
@router.message(Command("dog"))
async def send_dog(message: Message):
    url = "https://api.thedogapi.com/v1/images/search?limit=2&api_key="
    r = requests.get(url)
    data = r.json()
    dog_url = data[0]["url"]
    image = URLInputFile(dog_url, filename="dog.jpg")
    await bot.send_photo(message.chat.id, image)

# /cat command
@router.message(Command("cat"))
async def send_cat(message: Message):
    url = "https://api.thecatapi.com/v1/images/search?limit=1&api_key="
    r = requests.get(url)
    data = r.json()
    cat_url = data[0]["url"]
    image = URLInputFile(cat_url, filename="cat.jpg")
    await bot.send_photo(message.chat.id, image)

# Register router with dispatcher
dp.include_router(router)

# Entry point for aiogram v3
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
