from django.urls import path
from .views import index, contacts, woman, man, product_detail, product_list

urlpatterns = [
    path('', index, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('woman/', woman, name='woman'),
    path('man/', man, name='man'),

    path('products/', product_list, name='product_list'),  # Список всех товаров
    path('product/<int:pk>/', product_detail, name='product_detail'),  # Страница товара
]
