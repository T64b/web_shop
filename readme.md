**Stack:**

-mongodb
-mongoengine
-marhsmallow
-Telebot
-flask
-flask-restful
-google cloud
-linux
-nginx
-gunicorn

**Modules**
-Бд
-Бот
-REST API

**DB**
-Category
(title, description, subcategories, parent)
-Product
(title, description, parameters,  in_stock, is_available, price, discount, category)
-Cart
-Customer
(telegram_id, name, address)
-Text
(title, body)

**Tasks Lesson1**
1) Заполнить бд тестовыми данными
2) Реализовать в боте ответ на комманду /start, бот должен отвечать Inline клавиатурой из
всех доступных категорий (root (верхнего уровня)).
3) Подумать о применении колекции Text (Тянуть текст привествия оттуда).
