from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN = "5112181853:AAH0_tQF7ZD-t1ElMwWWjDDc16ME3mFyTNg"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

storage = MemoryStorage

admins = [762342298]
