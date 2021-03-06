import stripe
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from decimal import Decimal
from django.conf import settings
from django.contrib.auth.decorators import login_required

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.
def index(request):
    return render(request, "index.html")

def menu(request):
    return render(request, "menu.html")

@login_required(login_url='login')
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
        try:
            currentCart = user.cartOwner.get(cartPaid=False)
            currentPrice = currentCart.totalPrice + newPizza.pizzaPrice
            currentCart.totalPrice = currentPrice
            currentCart.pizzaOrdered.add(newPizza)
            currentCart.save()
        except:
            currentCart = Cart.objects.create(customer=user, totalPrice=newPizza.pizzaPrice)
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

@login_required(login_url='login')
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
            newSub.save()
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
        try:
            currentCart = user.cartOwner.get(cartPaid=False)
            currentPrice = currentCart.totalPrice + newSub.subPrice
            currentCart.totalPrice = currentPrice
            currentCart.subOrdered.add(newSub)
            currentCart.save()
        except:
            currentCart = Cart.objects.create(customer=user, totalPrice=newSub.subPrice)
            currentCart.subOrdered.add(newSub)
            currentCart.save()

        context = {
            'message':True,
        }
        return render(request, "sub.html", context)

    return render(request, "sub.html")

@login_required(login_url='login')
def pasta(request):
    if request.method == 'POST':
        user = request.user
        pastaName = request.POST['pastaName']
        getPasta = Pasta.objects.get(pastaName=pastaName)
        newPasta = CustomerPasta.objects.create(pastaName=pastaName, pastaPrice=getPasta.pastaPrice)

        # Add to cart
        currentCart = user.cartOwner.all().last()
        try:
            currentCart = user.cartOwner.get(cartPaid=False)
            currentPrice = currentCart.totalPrice + newPasta.pastaPrice
            currentCart.totalPrice = currentPrice
            currentCart.pastaOrdered.add(newPasta)
            currentCart.save()
        except:
            currentCart = Cart.objects.create(customer=user, totalPrice=newPasta.pastaPrice)
            currentCart.pastaOrdered.add(newPasta)
            currentCart.save()
        context = {
            "message":True,
        }
        return render(request, "pasta.html", context)
            
    return render(request, "pasta.html")

@login_required(login_url='login')
def salad(request):
    if request.method == 'POST':
        user = request.user
        saladName = request.POST['sName']
        print(saladName)
        getSalad = Salad.objects.get(saladName=saladName)
        newSalad = CustomerSalad.objects.create(saladName=saladName, saladPrice=getSalad.saladPrice)

        # Add to cart
        currentCart = user.cartOwner.all().last()
        try:
            currentCart = user.cartOwner.get(cartPaid=False)
            currentPrice = currentCart.totalPrice + newSalad.saladPrice
            currentCart.totalPrice = currentPrice
            currentCart.saladOrdered.add(newSalad)
            currentCart.save()
        except:
            currentCart = Cart.objects.create(customer=user, totalPrice=newSalad.saladPrice)
            currentCart.saladOrdered.add(newSalad)
            currentCart.save()

        context = {
            "message":True,
        }
        return render(request, "salad.html", context)
    return render(request, "salad.html")

@login_required(login_url='login')
def platter(request):
    if request.method == 'POST':
        user = request.user
        platterName = request.POST['platterName']
        platterSize = request.POST['platterSize']
        getPlatter = Platter.objects.get(platterName=platterName, platterSize=platterSize)
        newPlatter = CustomerPlatter.objects.create(platterName=platterName, platterSize=platterSize, platterPrice=getPlatter.platterPrice)

        # Add to cart
        currentCart = user.cartOwner.all().last()
        try:
            currentCart = user.cartOwner.get(cartPaid=False)
            currentPrice = currentCart.totalPrice + newPlatter.platterPrice
            currentCart.totalPrice = currentPrice
            currentCart.platterOrdered.add(newPlatter)
            currentCart.save()
        except:
            currentCart = Cart.objects.create(customer=user, totalPrice=newPlatter.platterPrice)
            currentCart.platterOrdered.add(newPlatter)
            currentCart.save()

        context = {
            "message":True,
        }
        return render(request, "platter.html", context)
    return render(request, "platter.html")

@login_required(login_url='login')
def cart(request):
    user = request.user

    if request.method == 'POST':
        currentCart = user.cartOwner.get(cartPaid=False)
        charge = stripe.Charge.create(
            amount=int(currentCart.totalPrice * 100),
            currency='usd',
            description='Order Paid!', 
            source=request.POST['stripeToken'] 
        )
        context = {
            "message":False,
            "isPaid":True,
        }
        currentCart.cartPaid = True
        currentCart.save()
        return render(request, 'cart.html', context)

    try:
        # currentCart = user.cartOwner.all().last()
        currentCart = user.cartOwner.get(cartPaid=False)
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

    stripeTotal = int(currentCart.totalPrice * 100)
    
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
        "stripeTotal":stripeTotal,
        "key": settings.STRIPE_PUBLISHABLE_KEY,
    }
    return render(request, "cart.html", context)

    