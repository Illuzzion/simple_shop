# Create your views here.
from django.views import generic

from .models import Product


class ProductIndexView(generic.ListView):
    queryset = Product.objects.filter(available=True)
    template_name = 'shop/product_list.html'


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'shop/product_detail.html'
