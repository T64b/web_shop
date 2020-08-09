from telebot import TeleBot
from telebot.types import (
    ReplyKeyboardMarkup,
    KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
)

from .config import TOKEN
from .db.models import Category, Product
from .texts import GREETINGS, CHOOSE_CATEGORY
from .keyboards import START_KB

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(*[KeyboardButton(button) for button in START_KB.values()])
    bot.send_message(message.chat.id, GREETINGS, reply_markup=kb)  #


@bot.message_handler(func=lambda m: m.text == START_KB['categories'])
def list_of_categories(message):
    kb = InlineKeyboardMarkup()
    categories = [
        InlineKeyboardButton(
            category.title,
            callback_data=f'{Category.__name__}{category.id}'
        ) for category in Category.get_root_categories()
    ]
    kb.add(*categories)
    bot.send_message(message.chat.id, CHOOSE_CATEGORY, reply_markup=kb)


@bot.message_handler(func=lambda m: m.text == START_KB['sales'])
def products_on_sale(message):
    kb = InlineKeyboardMarkup()
    categories = [
        InlineKeyboardButton(
            product.title,
            callback_data=f'{Product.__name__}{product.id}'
        ) for product in Product.get_products_discount()
    ]
    kb.add(*categories)
    bot.send_message(message.chat.id, CHOOSE_CATEGORY, reply_markup=kb)
