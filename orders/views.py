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
            currentPrice = currentCart.totalPrice + newPizza.pizzaPrice
            print(currentPrice)
            currentCart.totalPrice = currentPrice
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
        subSize = request.POST['subSize']
        print(subName)
        print(type(subName))
        extraCheese = request.POST['extraCheese']
        subPrice = Decimal(0)
        if subName == 'Steak + Cheese':
            steakTopping = request.POST.getlist('steakTopping')
            getSub = Sub.objects.get(subName=subName, subSize=subSize)
            # Create new sub
            subPrice = getSub.subPrice + Decimal((len(steakTopping) * 0.5))
            newSub = CustomerSub.objects.create(subName=subName, subSize=subSize, subPrice=subPrice)
            for top in steakTopping:
                newSub.subTopping.add(Topping.objects.get(topping=top))
        elif subName == 'Sausage, Peppers & Onions':
            subSize = 'l'
            getSub = Sub.objects.get(subName=subName, subSize=subSize)
            newSub = CustomerSub.objects.create(subName=subName, subSize=subSize, subPrice=getSub.subPrice)
        else:
            getSub = Sub.objects.get(subName=subName, subSize=subSize)
            newSub = CustomerSub.objects.create(subName=subName, subSize=subSize, subPrice=getSub.subPrice)

        # Check if added extra cheese
        if extraCheese == 'True':
            newSub.subPrice += Decimal(0.5)
            newSub.extraCheese = True
            newSub.save()

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

        context = {
            'message':True,
        }
        return render(request, "sub.html", context)

    return render(request, "sub.html")

def pasta(request):
    if request.method == 'POST':
        user = request.user
        pastaName = request.POST['pastaName']
        getPasta = Pasta.objects.get(pastaName=pastaName)
        newPasta = CustomerPasta.objects.create(pastaName=pastaName, pastaPrice=getPasta.pastaPrice)

        # Add to cart
        currentCart = user.cartOwner.all().last()
        if currentCart == None:
            newCart = Cart.objects.create(customer=user, totalPrice=newPasta.pastaPrice)
            newCart.pastaOrdered.add(newPasta)
            newCart.save()
        else:
            currentCart.totalPrice += newPasta.pastaPrice
            currentCart.pastaOrdered.add(newPasta)
            currentCart.save()
        context = {
            "message":True,
        }
        return render(request, "pasta.html", context)
            
    return render(request, "pasta.html")

def salad(request):
    if request.method == 'POST':
        user = request.user
        saladName = request.POST['sName']
        print(saladName)
        getSalad = Salad.objects.get(saladName=saladName)
        newSalad = CustomerSalad.objects.create(saladName=saladName, saladPrice=getSalad.saladPrice)

        # Add to cart
        currentCart = user.cartOwner.all().last()
        if currentCart == None:
            newCart = Cart.objects.create(customer=user, totalPrice=newSalad.saladPrice)
            newCart.saladOrdered.add(newSalad)
            newCart.save()
        else:
            currentCart.totalPrice += newSalad.saladPrice
            currentCart.saladOrdered.add(newSalad)
            currentCart.save()
        context = {
            "message":True,
        }
        return render(request, "salad.html", context)
    return render(request, "salad.html")

def platter(request):
    if request.method == 'POST':
        user = request.user
        platterName = request.POST['platterName']
        platterSize = request.POST['platterSize']
        getPlatter = Platter.objects.get(platterName=platterName, platterSize=platterSize)
        newPlatter = CustomerPlatter.objects.create(platterName=platterName, platterSize=platterSize, platterPrice=getPlatter.platterPrice)

        # Add to cart
        currentCart = user.cartOwner.all().last()
        if currentCart == None:
            newCart = Cart.objects.create(customer=user, totalPrice=newPlatter.platterPrice)
            newCart.platterOrdered.add(newPlatter)
            newCart.save()
        else:
            currentCart.totalPrice += newPlatter.platterPrice
            currentCart.platterOrdered.add(newPlatter)
            currentCart.save()
        context = {
            "message":True,
        }
        return render(request, "platter.html", context)
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
    checkPasta = currentCart.pastaOrdered.all()
    checkSalad = currentCart.saladOrdered.all()
    checkPlatter = currentCart.platterOrdered.all()
    pizza = len(checkPizza) != 0
    sub = len(checkSub) != 0
    pasta = len(checkPasta) != 0
    salad = len(checkSalad) != 0
    platter = len(checkPlatter) != 0

    print(pizza)
    print(sub)
    print(pasta)
    print(salad)

    context = {
        "cart":currentCart,
        "pizza":pizza,
        "sub":sub,
        "pasta":pasta,
        "salad":salad,
        "platter":platter,
        "checkSub":checkSub,
        "checkPasta":checkPasta,
        "checkSalad":checkSalad,
        "checkPlatter":checkPlatter,
    }
    return render(request, "cart.html", context)

def pay(request):
    return HttpResponse("paid")