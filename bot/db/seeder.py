from .models import Text, Category, Product


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

    s1 = Category.objects.create(title='Холодильники')
    s2 = Category.objects.create(title='Микроволновые печи')
    s3 = Category.objects.create(title='Плиты')

    c1.add_subcategory(s1)
    c1.add_subcategory(s2)
    c1.add_subcategory(s3)





