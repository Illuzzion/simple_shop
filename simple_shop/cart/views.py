# Create your views here.
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.views.decorators.http import require_POST
from shop.models import Product

from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def CartAdd(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'],
                 update_quantity=cd['update'])
        return redirect('cart:CartDetail')
    else:
        return render(request, 'shop/product_detail.html', {'cart_product_form': form, 'product': product})


# TODO: переделать на CBV
class CartAddCBV(generic.RedirectView):
    pass


class CartRemove(generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        product = get_object_or_404(Product, id=kwargs['product_id'])
        cart = Cart(self.request)
        cart.remove(product)
        return reverse('cart:CartDetail')


class CartView(generic.TemplateView):
    template_name = 'cart/detail.html'

    def get_context_data(self, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)
        # из-за формы обновления количества товара,
        # приходится добавлять форму к каждому товару и засылать корзину ещё раз
        cart = Cart(self.request)

        for item in cart:
            item['update_quantity_form'] = CartAddProductForm(
                initial={
                    'quantity': item['quantity'],
                    'update': True
                })

        context['cart'] = cart

        return context
