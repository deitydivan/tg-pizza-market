from config import dp, bot

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import inline_keyboard as kb
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

import logging
from data_base import sqlite_db_products, sqlite_db_orders
from handlers import client, admin, order


async def on_startup(_):
    print('bot online')
    sqlite_db_products.sql_start_products()
    sqlite_db_orders.sql_start_orders()


admin.register_handlers_client(dp)
client.register_handlers_client(dp)
order.register_handlers_client(dp)



executor.start_polling(dp, skip_updates=True, on_startup=on_startup)