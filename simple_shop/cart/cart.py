from decimal import Decimal

from django.conf import settings
from shop.models import Product


class Cart:
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
        # когда сериализуется сессия(JSONSerializer), все _ключи_ типа int преобразуются в строки
        # https://djbook.ru/rel1.9/topics/http/sessions.html#django.contrib.sessions.serializers.JSONSerializer
        all_prices = product.prices.all()
        price = str(all_prices[0].price)

        product_dict = self.cart.get(str(product.id), {'price': price, 'quantity': 0})
        product_dict['quantity'] = quantity if update_quantity else product_dict['quantity'] + quantity
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

    def __iter__(self):
        """
        Итерация по товарам корзины.
        Нужно для шаблона cart/details.html

        :return:
        """
        products = Product.objects.filter(id__in=self.cart.keys())

        for product in products:
            product_id = str(product.id)
            product_price = product.prices.all()[0].price
            self.cart[product_id]['product'] = product
            self.cart[product_id]['total_price'] = product_price * self.cart[product_id]['quantity']
            yield self.cart[product_id]

    def __len__(self):
        """
        Количество товаров в корзине

        :return: int
        """
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
