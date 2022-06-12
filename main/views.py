
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Pizza, Cart, CartItem
from django.db.models import Sum

# Create your views here.
def index(request):
    return HttpResponseRedirect('menu')


def view_cart(request):
    carts = CartItem.objects.filter(cart__user=request.user, cart__is_paid=False)
    total_price = carts.aggregate(Sum('Pizza__price'))
    total = total_price['Pizza__price__sum']
    context = {
        'carts': carts,
        'total': total,
    }
    return render(request, 'cart.html', context)


def food_menu(request):
    pizza_object = Pizza.objects.all()
    context = {
        'pizzas': pizza_object
    }
    return render(request, 'menu.html', context)

@login_required(login_url='login')
def add_cart(request, pizza_uuid):
    user = request.user
    pizza_obj = Pizza.objects.get(uuid=pizza_uuid)
    cart, _ = Cart.objects.get_or_create(user=user, is_paid=False)
    cart_items = CartItem.objects.create(cart=cart, Pizza=pizza_obj)
    print(cart_items)
    
    return redirect('/')

def cusLogin(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(username, password)
            user_object = User.objects.filter(username=username)
            if not user_object.exists():
                messages.error(request, 'Donot have credential')
                return redirect('login')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'credential error')
                return redirect('login')
        except Exception as e:
            print(f'something went wrong {e}')
    return render(request, 'login.html', {'title': 'login'})


def registration(request):
    if request.method == "POST":
        try:
            username = request.POST.get('username')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            is_username = User.objects.filter(username=username)
            if is_username.exists():
                print('already exists')
                messages.error(request, 'already exists')
                return redirect('registration')
            if password1 == password2:
                create_user = User.objects.create(username=username)
                create_user.set_password(password1)
                create_user.save()
                print('data saved')
                messages.success(request, 'your account created now you can login')
            else:
                messages.error(request, 'password should be matched')
                return redirect('registration')
        except Exception as e:
            print(f'something went wrong {e}')
            messages.error(request, 'something went wrong')
    return render(request, 'registration.html', {'title': 'registration'})
    

def log_out(request):
    logout(request)
    return HttpResponseRedirect('login')