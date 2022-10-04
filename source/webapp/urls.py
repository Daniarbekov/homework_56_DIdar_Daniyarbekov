

from django.urls import path
from webapp.views.base import index_view
from webapp.views.product import product_create_view

urlpatterns = [
    path("", index_view, name='index'),
    path('product/create', product_create_view, name='create_product')
]
