from tkinter import FALSE, TRUE
from config import dp, bot
from keyboards import inline_key as kb

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text

import sqlite3 as sq
from data_base import sqlite_db_products,sqlite_db_orders

class FSMOrder(StatesGroup):
    id = State()
    pizza = State()
    amount = State()
    status = State()


async def create_order(message: types.Message, state=None):
    await bot.send_message(message.from_user.id, "Здравствуйте\nCледуй дальнейшим инструкциям что-бы сделать заказ")
    await bot.send_message(message.from_user.id, "Введите название пиццы которую хотите заказать")
    await FSMOrder.pizza.set()

async def order_pizza(message: types.Message, state=FSMOrder.pizza):
    async with state.proxy() as data:
        data['id'] = message.from_user.id
        data['pizza'] = message.text
    await bot.send_message(message.from_user.id,"Введите количество которое желаете заказать:")
    await FSMOrder.amount.set()

async def order_amount(message: types.Message, state=FSMOrder.amount):
    async with state.proxy() as data:
        data['amount'] = message.text
        data['status'] = 'принят'
    await sqlite_db_orders.sql_add_order(state)
    await state.finish()
    await bot.send_message(message.from_user.id,"Спасибо, ваш заказ принят")

# @dp.callback_query_handler(lambda c: c.data == 'order')
async def order_button(callback_query: types.CallbackQuery, state=FSMOrder):
    await bot.send_message(callback_query.from_user.id, "Здравствуйте\nCледуй дальнейшим инструкциям что-бы сделать заказ")
    await bot.send_message(callback_query.from_user.id, "Введите название пиццы которую хотите заказать")
    await FSMOrder.pizza.set()




def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(create_order, commands=['order'], state=None)
    dp.register_message_handler(order_pizza, state=FSMOrder.pizza)
    dp.register_message_handler(order_amount, state=FSMOrder.amount)
    dp.register_callback_query_handler(order_button, lambda c: c.data == 'order')