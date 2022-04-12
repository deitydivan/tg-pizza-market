from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

# инлайн кнопки для выбора категории
inline_btn_meet = InlineKeyboardButton('мясные', callback_data='meet')
inline_btn_chease = InlineKeyboardButton('сырные', callback_data='chease')
inline_btn_vegan = InlineKeyboardButton('грибная', callback_data='vegan')
inline_kb_cat = InlineKeyboardMarkup(row_width=2)
inline_kb_cat.add(inline_btn_meet,inline_btn_chease,inline_btn_vegan)


# инлайн кнопка заказа пиццы
inline_btn_order = InlineKeyboardButton('заказать', callback_data='order')
inline_kb_order = InlineKeyboardMarkup(row_width=2)
inline_kb_order.add(inline_btn_order)
