from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN = "2125042790:AAGhXD57wRAbT3J0TuyOWyo4PT_KahTT8O8"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

storage = MemoryStorage
