from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
class BaseModel(models.Model):
    uuid = models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class PizzaCatagory(BaseModel):
    catagory_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.catagory_name

class Pizza(BaseModel):
    catagory = models.ForeignKey(PizzaCatagory, on_delete=models.CASCADE, related_name='pizzas')
    pizza_name = models.CharField(max_length=100)
    price = models.IntegerField(default=100)
    image = models.ImageField(upload_to='pizza')

    def __str__(self):
        return self.pizza_name


class Cart(BaseModel):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='carts')
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f'user: {self.user} and paid: {self.is_paid}'


class CartItem(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    Pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)

    def __str__(self):
        return f'cart: {self.cart} and pizza: {self.Pizza}'

