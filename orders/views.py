from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from decimal import Decimal

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
        return render(request, "pizza.html", context)

    # When request is GET
    toppings = Topping.objects.all()
    context = {
        'toppings':toppings,
    }
    return render(request, "pizza.html", context)

def sub(request):
    if request.method == 'POST':
        user = request.user
        subName = request.POST['subName']
        print(subName)
        print(type(subName))
        extraCheese = request.POST['extraCheese']
        if subName == 'Steak + Cheese':
            print("heyyy")
            steakTopping = request.POST.getlist('steakTopping')
            subSize = request.POST['subSize']
            getSub = Sub.objects.get(subName=subName, subSize=subSize)
            # Create new sub
            subPrice = getSub.subPrice + Decimal((len(steakTopping) * 0.5))
            newSub = CustomerSub.objects.create(subName=subName, subSize=subSize, subPrice=subPrice)
            if extraCheese == 'True':
                newSub.subPrice += Decimal(0.5)
                newSub.extraCheese = True
                newSub.save()
            for top in steakTopping:
                newSub.subTopping.add(Topping.objects.get(topping=top))
            
            # Add to cart
            currentCart = user.cartOwner.all().last()
            if currentCart == None:
                newCart = Cart.objects.create(customer=user, totalPrice=newSub.subPrice)
                newCart.subOrdered.add(newSub)
                newCart.save()
            else:
                currentCart.totalPrice += newSub.subPrice
                currentCart.subOrdered.add(newSub)
                currentCart.save()
        elif subName == 'Sausage, Peppers & Onions':
            pass
        else:
            print("other")

        context = {
            'message':True,
        }
        return render(request, "sub.html", context)

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

def cart(request):
    user = request.user
    try:
        currentCart = user.cartOwner.all().last()
        checkPizza = currentCart.pizzaOrdered.all()
    except:
        context = {
            "message": True,
        }
        return render(request, "cart.html", context)

    checkSub = currentCart.subOrdered.all()
    pizza = len(checkPizza) != 0
    sub = checkSub != None
    print(checkSub)
    context = {
        "cart":currentCart,
        "pizza":pizza,
        "sub":sub,
        "checkSub":checkSub
    }
    return render(request, "cart.html", context)