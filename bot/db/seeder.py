from bot.db.models import Text


def seed_texts():
    greetings = {
        'title': 'greetings',
        'body': ' Приветствую пользователь'
    }

    discount = {
        'title': 'discount',
        'body': 'Товары со скидкой'
    }

    Text.objects.create(**greetings)
    Text.objects.create(**discount)
