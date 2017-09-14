from decimal import Decimal

from django.conf import settings
from shop.models import Product


class Cart(object):
    """
    Корзина
    """

    def __init__(self, request):
        self.session = request.session
        self.cart = self.session.get(settings.CART_SESSION_ID, dict())

    def add(self, product, quantity=1, update_quantity=False):
        """
        Добавление товара в корзину

        :param product: Товар
        :param quantity: Количество
        :param update_quantity: Флаг обновления количества
        :return: None
        """
        product_dict = self.cart.get(product.id, {'price': str(product.price), 'quantity': 0})
        product_dict['quantity'] = quantity if update_quantity else product_dict['quantity'] + quantity
        # когда сохраняется сессия, все _ключи_ типа int преобразуются в строки
        # https://djbook.ru/rel1.9/topics/http/sessions.html#django.contrib.sessions.serializers.JSONSerializer
        self.cart.update({product.id: product_dict})
        self.save()

    def save(self):
        """
        Сохранение данных корзины в сессию

        :return:
        """
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        """
        Удаление товара из корзины

        :param product: Товар который нужно удалить
        :return:
        """
        if str(product.id) in self.cart:
            del self.cart[str(product.id)]
            self.save()

    # Итерация по товарам
    def __iter__(self):
        # product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=self.cart.keys())

        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    # Количество товаров
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        """
        Очистка корзины
        :return:
        """
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
