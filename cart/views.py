from django.shortcuts import render, redirect
from .models import Cart

def home(request):
    if request.user.is_anonymous:
        return redirect('index')
    cart_obj = Cart.objects.new_or_get(request)
    return render(request, "cart/home.html")