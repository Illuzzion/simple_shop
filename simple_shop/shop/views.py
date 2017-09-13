# Create your views here.
from django.views import generic

from cart.forms import CartAddProductForm
from .models import Product, Category


class ProductIndexView(generic.ListView):
    queryset = Product.objects.filter(available=True)
    template_name = 'shop/product_list.html'


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'shop/product_detail.html'

    def get(self, request, *args, **kwargs):
        return self.render_to_response({
            'product': Product.objects.get(pk=self.kwargs['pk']),
            'cart_product_form': CartAddProductForm(),
        })


class CategoryIndexView(generic.ListView):
    model = Category
    template_name = 'shop/category_list.html'


class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = 'shop/category_detail.html'

    # def get(self, request, *args, **kwargs):
    #     category = Category.objects.get(slug=self.kwargs['slug'])
    #     return self.render_to_response({'category': category})
