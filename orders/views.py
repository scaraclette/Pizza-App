from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, "index.html")

def menu(request):
    return render(request, "menu.html")

def pizza(request):
    if request.method == 'POST':
        return render(request, "pizza.html")

    # When request is GET
    toppings = Topping.objects.all()
    context = {
        'toppings':toppings,
    }
    return render(request, "pizza.html", context)

def sub(request):
    if request.method == 'GET':
        return render(request, "sub.html")

def pasta(request):
    if request.method == 'GET':
        return render(request, "pasta.html")

def salad(request):
    if request.method == 'GET':
        return render(request, "salad.html")

def platter(request):
    if request.method == 'GET':
        return render(request, "platter.html")
