from django.conf.urls import url

from . import views

app_name = 'shop'

urlpatterns = [
    url(r'^$', views.ProductIndexView.as_view(), name='index'),
    url(r'product/(?P<pk>[0-9]+)/', views.ProductDetailView.as_view(), name='product_details')
]
