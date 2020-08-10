from telebot import TeleBot
from telebot.types import (
    ReplyKeyboardMarkup,
    KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
)

from .config import TOKEN
from .db.models import Category, Product, News
from .texts import GREETINGS, CHOOSE_CATEGORY, CHOOSE_PRODUCT, CHOOSE_NEWS
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
    products = [
        InlineKeyboardButton(
            product.title,
            callback_data=f'{Product.__name__}{product.id}'
        ) for product in Product.get_products_discount()
    ]
    kb.add(*products)
    bot.send_message(message.chat.id, CHOOSE_PRODUCT, reply_markup=kb)


@bot.message_handler(func=lambda m: m.text == START_KB['news'])
def last_news(message):
    kb = InlineKeyboardMarkup()
    news = [
        InlineKeyboardButton(
            news.title,
            callback_data=f'{News.__name__}{news.id}'
        ) for news in News.get_last_three_news()
    ]
    kb.add(*news)
    bot.send_message(message.chat.id, CHOOSE_NEWS, reply_markup=kb)
