from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cart/', views.view_cart, name='view_cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),  # Убедись, что имя 'add_to_cart' указано здесь
]