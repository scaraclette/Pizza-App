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
        user = request.user
        toppings = request.POST.getlist('toppings')
        pizzaType = request.POST['pizzaType']
        pizzaSize = request.POST['pizzaSize']
        special = request.POST['isSpecial']
        isSpecial = False
        if special == True:
            isSpecial = True
        getPizza = Pizza.objects.get(pizzaType=pizzaType, pizzaSize=pizzaSize, isSpecial=isSpecial, totalTopping = len(toppings))
        newPizza = CustomerPizza.objects.create(customer=user, pizzaType=pizzaType, pizzaSize=pizzaSize, isSpecial=isSpecial, pizzaPrice=getPizza.pizzaPrice)
        for top in toppings:
            newPizza.pizzaTopping.add(Topping.objects.get(topping=top))

        # Add to cart
        currentCart = user.cartOwner.all().last()
        # if cart doesn't exist, create new cart and add the totalPrice
        if currentCart == None:
            newCart = Cart.objects.create(customer=user, totalPrice=newPizza.pizzaPrice)
            newCart.pizzaOrdered.add(newPizza)
            newCart.save()
        else:
            currentCart.totalPrice += newPizza.pizzaPrice
            currentCart.pizzaOrdered.add(newPizza)
            currentCart.save()

        context = {
            'message':True,
            'toppings':Topping.objects.all()
        }
        return render(request, "test.html", context)

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
