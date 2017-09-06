# Create your views here.
from django.views import generic

from .models import Product


class ProductIndexView(generic.ListView):
    template_name = 'shop/index.html'
    queryset = Product.objects.order_by('-id')
