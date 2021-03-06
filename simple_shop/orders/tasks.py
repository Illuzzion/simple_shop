from celery import task
from django.core.mail import send_mail

from .models import Order


@task
def OrderCreated(order_id):
    """
    Отправка Email сообщения о создании покупке

    """
    order = Order.objects.get(id=order_id)
    subject = 'Заказ c номером {}'.format(order.id)
    message = 'Дорогой, {name}, вы успешно сделали заказ. Номер вашего заказа {id}'.format(
        name=order.first_name,
        id=order.id
    )
    mail_send = send_mail(subject, message, 'admin@myshop.ru', [order.email])
    return mail_send
