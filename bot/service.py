from typing import List
from .db.models import Category
from telebot import TeleBot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

from .lookups import CATEGORY_LOOKUP, SEPARATOR


class WebShopBot(TeleBot):

    @staticmethod
    def generate_categories_kb(categories: List[Category], **kwargs):
        kb = InlineKeyboardMarkup(**kwargs)
        buttons = [InlineKeyboardButton(
            text=c.title,
            callback_data=f'{CATEGORY_LOOKUP}{SEPARATOR}{c.id}'
        ) for c in categories]
        kb.add(*buttons)
        return kb

    def generate_and_send_categories_kb(self, text: str, chat_id: int,
                                        categories: List[Category], **kwargs):
        self.send_message(
            chat_id,
            text,
            reply_markup=self.generate_categories_kb(categories, **kwargs))

    def generate_and_edit_categories_kb(self, text: str, chat_id: int,
                                        message_id: int,
                                        categories: List[Category], **kwargs):
        self.edit_message_text(
            text,
            chat_id,
            message_id,
            reply_markup=self.generate_categories_kb(
                categories, **kwargs))
