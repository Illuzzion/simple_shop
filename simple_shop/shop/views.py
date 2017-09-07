# Create your views here.
from django.views import generic

from .models import Product, Category


class ProductIndexView(generic.ListView):
    queryset = Product.objects.filter(available=True)
    template_name = 'shop/product_list.html'


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'shop/product_detail.html'


class CategoryIndexView(generic.ListView):
    model = Category
    template_name = 'shop/category_list.html'


class CategoryDetailView(generic.DetailView):
    model = Category
    template_name =