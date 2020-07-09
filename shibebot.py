import logging,requests,json

from aiogram import Bot, Dispatcher, executor, types

# Enter your API token
API_TOKEN = ''

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm ShibeBot by @bosniandoge!\nPowered by aiogram.")

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
	await message.reply("To use this bot do:\n /doge - if you want a shibe picture")


@dp.message_handler(commands=['doge'])
async def cmd_image(message: types.Message):
	url = 'https://shibe.online/api/shibes?count=1&urls=true&httpsUrls=true'
	r = requests.get(url)
	dogeurl = r.content
	urlsecond = dogeurl[2:-2].decode('utf-8')
	print(urlsecond)
	dogeimg = requests.get(urlsecond)
	print(dogeimg)
	await bot.send_photo(message.chat.id, types.InputFile.from_url(str(urlsecond)))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
