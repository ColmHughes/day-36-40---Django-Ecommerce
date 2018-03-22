from django.conf.urls import url, include

from .views import *


urlpatterns = [
    url(r'^$', product_list, name='product_list'),
    url(r'^(\d+)$', product_item, name='product_item'),
]