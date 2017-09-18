from django.views import generic

from .models import Category


class CategoryIndexView(generic.ListView):
    model = Category
    template_name = 'categories/category_list.html'


class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = 'categories/category_detail.html'
