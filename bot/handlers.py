from telebot.types import (
    ReplyKeyboardMarkup,
    KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
)

from .config import TOKEN
from .db.models import Category, Product, News, Text
from .keyboards import START_KB
from .lookups import PRODUCT_LOOKUP, SEPARATOR, CATEGORY_LOOKUP
from .service import WebShopBot
bot_instance = WebShopBot(TOKEN)


@bot_instance.message_handler(commands=['start'])
def start(message):
    txt = Text.objects.get(title=Text.GREETINGS)
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    kb.add(*[KeyboardButton(button) for button in START_KB.values()])
    bot_instance.send_message(message.chat.id, txt.body, reply_markup=kb)


@bot_instance.message_handler(func=lambda m: m.text == START_KB['categories'])
def get_root_categories(message):
    # txt = Text.objects.get(title=Text.GREETINGS)
    categories = Category.get_root_categories()
    bot_instance.generate_and_send_categories_kb('Choose category',
                                                 message.chat.id,
                                                 categories)


@bot_instance.callback_query_handler(
    lambda call: call.data.startswith(CATEGORY_LOOKUP))
def categories(call):
    category_id = call.data.split(SEPARATOR)[1]
    category = Category.objects.get(id=category_id)

    if category.subcategories:
        bot_instance.generate_and_edit_categories_kb(
            category.title,
            call.message.chat.id,
            call.message.message_id,
            category.subcategories
        )
        # if category.parent:
        #     kb.add(
        #         InlineKeyboardButton(
        #             'Back',
        #             callback_data=f'{CATEGORY_LOOKUP}{SEPARATOR}{category_id}'))

    else:
        products = category.get_products()
        for product in products:
            kb = InlineKeyboardMarkup()
            button = InlineKeyboardButton(
                text=product.title,
                callback_data=f'{PRODUCT_LOOKUP}{SEPARATOR}{product.id}')

            kb.add(button)
            bot_instance.send_photo(call.message.chat.id,
                                    product.get_image(),
                                    product.title,
                                    reply_markup=kb)


@bot_instance.message_handler(content_types=['text'], func=lambda m: m.text == START_KB['sales'])
def products_on_sale(message):
    txt = Text.objects.get(title=Text.GREETINGS)

    discount_products = Product.get_products_discount()
    for product in discount_products:
        kb = InlineKeyboardMarkup()
        button = InlineKeyboardButton(
            text=product.title,
            callback_data=f'{PRODUCT_LOOKUP}{SEPARATOR}{product.id}')
        kb.add(button)
        bot_instance.send_photo(
            message.chat.id,
            product.get_image(),
            product.title,
            reply_markup=kb)


@bot_instance.message_handler(func=lambda m: m.text == START_KB['news'])
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
    bot_instance.send_message(message.chat.id, txt.body, reply_markup=kb)
