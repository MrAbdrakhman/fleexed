from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserLoginForm
from django.contrib.auth import login, logout

# Create your views here.
from .models import Product, Price


def index(request):
    # products = Product.objects.all()[:4]
    # coaches = Coach.objects.all()[:4]
    # context = {
    #     'products': products,
    #     'coaches': coaches
    # }
    return render(request, 'web_yoga/index.html')

def about(request):
    return render(request, 'web_yoga/about.html')

def product(request):
    products = Product.objects.all()
    return render(request, 'web_yoga/product.html', {'products': products})

def pricing(request):
    pr = Price.objects.all()
    return render(request, 'web_yoga/pricing.html', {'pr': pr})

def yoga_online(request):
    return render(request, 'web_yoga/yoga_online.html')

def login_user(request):
    if request.method == 'POST':
        form =UserLoginForm(data=request.POST)
        if form.is_valid():
            user =form.get_user()
            login(request, user)
            messages.success(request, 'Успех')
            return redirect('/')
        else:
            messages.error(request,'No')
    else:
         form = UserLoginForm()
    return render(request, 'web_yoga/login.html', {'form': form})

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Вы успешно зарегистрировались')
            return  redirect('login')
        else:
            messages.error(request, "Есть ошибка в регистрации")
    else:
        form = UserCreationForm()
    return render(request,'web_yoga/register.html', {'form': form})

def contact(request):
    return render(request, 'web_yoga/contact.html')

def logout_user(request):
    logout(request)
    return redirect('/')