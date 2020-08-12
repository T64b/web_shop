from telebot import TeleBot
from telebot.types import (
    ReplyKeyboardMarkup,
    KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
)

from .config import TOKEN, DEFAULT_PHOTO_URL
from .db.models import Category, Product, News, Text
from .keyboards import START_KB
from .lookups import PRODUCT_LOOKUP, SEPARATOR

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    txt = Text.objects.get(title=Text.GREETINGS)
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    kb.add(*[KeyboardButton(button) for button in START_KB.values()])
    bot.send_message(message.chat.id, txt.body, reply_markup=kb)


@bot.message_handler(func=lambda m: m.text == START_KB['categories'])
def list_of_categories(message):
    txt = Text.objects.get(title=Text.GREETINGS)

    kb = InlineKeyboardMarkup()
    categories = [
        InlineKeyboardButton(category.title,
                             callback_data=f'{Category.__name__}{category.id}'
                             ) for category in Category.get_root_categories()
    ]
    kb.add(*categories)
    bot.send_message(message.chat.id, txt.body, reply_markup=kb)


@bot.message_handler(content_types=['text'],
                     func=lambda m: m.text == START_KB['sales'])
def products_on_sale(message):
    txt = Text.objects.get(title=Text.GREETINGS)

    discount_products = Product.get_products_discount()
    for product in discount_products:
        kb = InlineKeyboardMarkup()
        button = InlineKeyboardButton(
            text=product.title,
            callback_data=f'{PRODUCT_LOOKUP}{SEPARATOR}{product.id}'
        )
        kb.add(button)
        bot.send_photo(
            message.chat.id,
            product.get_image(),
            product.title,
            reply_markup=kb
        )


@bot.message_handler(func=lambda m: m.text == START_KB['news'])
def last_news(message):
    txt = Text.objects.get(title=Text.GREETINGS)

    kb = InlineKeyboardMarkup()
    news = [
        InlineKeyboardButton(
            news.title,
            callback_data=f'{News.__name__}{news.id}'
        ) for news in News.get_last_three_news()
    ]
    kb.add(*news)
    bot.send_message(message.chat.id, txt.body, reply_markup=kb)
