from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^create/$', views.OrderCreate, name='OrderCreate'),
    url(r'^admin/order/(?P<order_id>\d+)/$', views.admin_order_detail, name='AdminOrderDetail')
]
