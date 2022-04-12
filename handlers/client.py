from itertools import count
from config import dp, bot
from keyboards import inline_key as kb

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text

from handlers import client, admin, order
import sqlite3 as sq
from data_base import sqlite_db_products,sqlite_db_orders

# callback для мясных пицц
# @dp.callback_query_handler(lambda c: c.data == 'meet')
async def meet_button(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    pizzas = sqlite_db_products.cur.execute('SELECT * FROM products').fetchall()
    for row in pizzas:
        if row[2] == 'мясные':
            await bot.send_photo(callback_query.from_user.id, row[3],caption=row[0] + "\n" + row[1],reply_markup=kb.inline_kb_order)

# callback для мясных сырных пицц
# @dp.callback_query_handler(lambda c: c.data == 'chease')
async def chease_button(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    pizzas = sqlite_db_products.cur.execute('SELECT * FROM products').fetchall()
    for row in pizzas:
        if row[2] == 'сырные':
            await bot.send_photo(callback_query.from_user.id, row[3],caption=row[0] + "\n" + row[1],reply_markup=kb.inline_kb_order)


# callback для мясных грибных пицц
# @dp.callback_query_handler(lambda c: c.data == 'vegan')
async def vegan_button(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    pizzas = sqlite_db_products.cur.execute('SELECT * FROM products').fetchall()
    for row in pizzas:
        if row[2] == 'веганские':
            await bot.send_photo(callback_query.from_user.id, row[3],caption=row[0] + "\n" + row[1],reply_markup=kb.inline_kb_order)

async def get_pizzas(message: types.Message):
    await bot.send_message(message.from_user.id, "Выберите категорию пиццы", reply_markup=kb.inline_kb_cat)

async def cheack_orders_command(message: types.Message, state=None):
    orders = sqlite_db_orders.cur.execute('SELECT * FROM orders').fetchall()
    counter = 0
    for i in orders:
        if str(message.from_user.id) == i[0] and i[3] != 'выполнен':
            await bot.send_message(message.from_user.id, "pizza: " + i[1] +" " + i[2] + "шт" +"\nстатус: " + i[3])
            counter += 1
    if counter == 0:
        await bot.send_message(message.from_user.id, "У вас нет активных заказов" )
        



# order.register_handlers_client(dp)
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(get_pizzas, commands=['pizzas'], state=None)
    dp.register_message_handler(cheack_orders_command, commands=['orders'], state=None)
    dp.register_callback_query_handler(meet_button, lambda c: c.data == 'meet')
    dp.register_callback_query_handler(chease_button, lambda c: c.data == 'chease')
    dp.register_callback_query_handler(vegan_button, lambda c: c.data == 'vegan')
