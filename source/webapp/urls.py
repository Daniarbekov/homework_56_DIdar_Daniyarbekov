

from django.urls import path
from webapp.views.base import index_view
from webapp.views.product import product_create_view, product_update_view, product_delete_view, product_detail_view


urlpatterns= [
    path("", index_view, name='index'),
    path("task_create", product_create_view, name='create_product'),
    path('task_detail/<int:pk>',product_detail_view, name='detail'),
    path('task_deatil/<int:pk>/update', product_update_view, name='update_product'),
    path('task/<int:pk>/delete', product_delete_view, name='delete_product')
]
