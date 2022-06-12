from django.contrib import admin
from .models import Pizza, PizzaCatagory, Cart, CartItem
# Register your models here.
admin.site.register(Pizza)
admin.site.register(PizzaCatagory)
admin.site.register(Cart)
admin.site.register(CartItem)