from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^create/$', views.order_create, name='OrderCreate'),
    # url(r'^create2/$', views.OrderCreateView.as_view(), name='OrderCreate'),
    # url(r'^success/$', views.OrderCreateView.as_view(), name='OrderCreate'),
    url(r'^admin/order/(?P<order_id>\d+)/$', views.admin_order_detail, name='AdminOrderDetail')
]
