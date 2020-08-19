from bot.db.models import Text, Category, Product


def seed_texts():
    greetings = {
        'title': 'greetings',
        'body': 'Приветствую пользователь'
    }

    discount = {
        'title': 'discount',
        'body': 'Товары со скидкой'
    }

    Text.objects.create(**greetings)
    Text.objects.create(**discount)


def seed_categories():
    c1 = Category.objects.create(title='Бытовая техника')
    c2 = Category.objects.create(title='Телефоны')
    c3 = Category.objects.create(title='Ноутбуки и компьютеры')

    s1 = Category.objects(title='Холодильники')



