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

**Tasks Lesson2**

Организовать навигационную клавиатуру (из кнопок шаблонов). Следующие кнопки:
Категории
Товары со скидкой
Новости
Предусмотреть логику нажатия на каждую кнопку
Кнопка "Категории" - бот должен отвечать Inline клавиатурой из всех доступных категорий (root (верхнего уровня))
"Товары со скидкой" - инлайн клавиатура из товаров со скидкой
Выводить сообщение с последними тремя новостями (создать и описать колекцию новостей)
**Tasks lesson 3**

Предусмотреть поле картинки у модели продуктов
Для каждого продукта писать в чат:
Картинка
Описание позиции
Кнопка с приявзкой к айди товара
При клике на кнопку "категории" выводить список всех досупных категорий. 3.1) При клике на категорию у которой нету подкатегорий выводить все продукты из неё.
1 сообщение с продуктом = Картинка + Описание + Кнопка