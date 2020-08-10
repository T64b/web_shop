import mongoengine as me
from decimal import Decimal

me.connect('webshop_db')


class Category(me.Document):
    title = me.StringField(min_length=2, max_length=512, required=True)
    description = me.StringField(min_length=8, max_length=2048)
    subcategories = me.ListField(me.ReferenceField('self'))
    parent = me.ReferenceField('self')

    def get_products(self):
        return Product.objects.filter(category=self)

    @classmethod
    def get_root_categories(cls):
        return cls.objects(parent=None)

    def add_subcategory(self, subcategory: 'Category'):
        # self -> current category
        # subcat -> category gonna be as subcategory
        subcategory.parent = self
        subcategory.save()

        self.subcategories.append(subcategory)
        self.save()


class Parameter(me.EmbeddedDocument):
    height = me.FloatField()
    width = me.FloatField()
    weight = me.FloatField()
    length = me.FloatField()


class Product(me.Document):
    title = me.StringField(min_length=2, max_length=512, required=True)
    description = me.StringField(min_length=8, max_length=2048)
    in_stock = me.IntField(min_value=0, required=True)
    is_available = me.BooleanField(default=True)
    discount = me.IntField(min_value=0, max_value=99, default=0)
    price = me.DecimalField(min_value=1, force_string=True)
    parameter = me.EmbeddedDocumentField(Parameter)
    category = me.ReferenceField(Category)

    @property
    def actual_price(self):
        return (self.price * Decimal((100 - self.discount) / 100)).quantize(
            Decimal('.01'), 'ROUND_HALF_UP')

    @classmethod
    def get_products_discount(cls):
        return cls.objects(discount__ne=0)


class News(me.Document):
    title = me.StringField(min_length=2, max_length=512, required=True)
    description = me.StringField(min_length=5, max_length=4096, required=True)

    @classmethod
    def get_last_three_news(cls):
        return cls.objects.order_by('-id')[:3]
