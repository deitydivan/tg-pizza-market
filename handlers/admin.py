import os
from pydoc import describe
from config import dp, bot,admins
# from keyboards import inline_key as kb
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
import sqlite3 as sq
from data_base import sqlite_db_products


class FSMAdd(StatesGroup):
    name = State()
    description = State()
    category = State()
    img = State()


async def create_post_command(message: types.Message, state=None):
    if message.from_user.id in admins:
        await bot.send_message(message.from_user.id, "Привет\n Cледуй дальнейшим инструкциям что-бы дoбавить новый продукт")
        await bot.send_message(message.from_user.id,"Введите имя продукта:")
        await FSMAdd.name.set()
    else:
        await bot.send_message(message.from_user.id,"Вы не админ этого бота\nУ вас нет доступа к этой команде")

async def get_name_product(message: types.Message, state=FSMAdd.name):
    async with state.proxy() as data:
        data['name'] = message.text
    await bot.send_message(message.from_user.id,"Введите описание продукта:")
    await FSMAdd.description.set()

async def get_description_product(message: types.Message, state=FSMAdd.description):

    async with state.proxy() as data:
        data['description'] = message.text
    await bot.send_message(message.from_user.id,"Введите категорию продукта:")
    await FSMAdd.category.set()

async def get_category_product(message: types.Message, state=FSMAdd.category):
    async with state.proxy() as data:
        data['category'] = message.text
    await bot.send_message(message.from_user.id,"Отпровьте фото продукта:")
    await FSMAdd.img.set()


# @dp.message_handler(content_types=['photo'])
async def get_img_product(message, state=FSMAdd.img):
    await message.photo[-1].download('product.jpg')
    with open("product.jpg", 'rb') as file:
        blob_data = file.read()
    async with state.proxy() as data:
        data['img'] = blob_data
    await sqlite_db_products.sql_add_command(state)
    await state.finish()
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../product.jpg')
    os.remove(path)

async def send(message: types.Message):
    rec = sqlite_db_products.cur.execute('SELECT * FROM products').fetchall()
    for row in rec:
        if row[0] == 'dfgdfv':
            await bot.send_photo(message.from_user.id, row[3])

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(create_post_command, commands=['add'], state=None)
    dp.register_message_handler(get_name_product, state=FSMAdd.name)
    dp.register_message_handler(get_description_product, state=FSMAdd.description)
    dp.register_message_handler(get_category_product, state=FSMAdd.category)
    dp.register_message_handler(get_img_product,content_types=['photo'], state=FSMAdd.img)
    dp.register_message_handler(send,commands=['send'])
    
