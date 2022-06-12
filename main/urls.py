from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.cusLogin, name='login'),
    path('registration', views.registration, name='registration'),
    path('logout', views.log_out, name='logout'),
    path('menu', views.food_menu, name='menu'),
    path('add-cart/<pizza_uuid>', views.add_cart, name='add_cart' ),
    path('cart', views.view_cart, name='cart'),
]