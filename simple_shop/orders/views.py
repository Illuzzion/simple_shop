from cart.cart import Cart
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404
from django.views import generic

from .forms import OrderCreateForm
from .models import OrderItem, Order
from .tasks import OrderCreated


# TODO: перевести всё на CBV

def order_create(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)

        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()

            # Асинхронная отправка email сообщения
            OrderCreated.delay(order.id)

            return render(request, 'orders/order/created.html', {'order': order})

    form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})


# class OrderCreateView(generic.CreateView):
#     form_class = OrderCreateForm
#     template_name = 'orders/order/create.html'
#
#     def get_success_url(self):
#         print('get_success_url')


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'admin/orders/order/detail.html', {'order': order})
