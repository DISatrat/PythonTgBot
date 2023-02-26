from aiogram import Bot,types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import config

# Bot = Bot('6144355865:AAGc-S-JW19KaT3LjWRTrCrY9iZJQZdimQY')
Bot = Bot(config.token)
bot = Dispatcher(Bot)