from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^remove/(?P<product_id>\d+)/$', views.CartRemove, name='CartRemove'),
    url(r'^remove/(?P<product_id>\d+)/$', views.CartRemove.as_view(), name='CartRemove'),
    url(r'^add/(?P<product_id>\d+)/$', views.CartAdd, name='CartAdd'),
    url(r'^$', views.CartView.as_view(), name='CartDetail'),
]
