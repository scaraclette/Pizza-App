from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topping(models.Model):
    topping = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.topping}"

class Pizza(models.Model):
    REGULAR = 'R'
    SICILIAN = 'S'
    SMALL = 's'
    LARGE = 'l'

    PIZZA_TYPE = (
        (REGULAR, 'regular'),
        (SICILIAN, 'sicilian'),
    )

    PIZZA_SIZE = (
        (SMALL, 'small'),
        (LARGE, 'large')
    )
    pizzaType = models.CharField(max_length=1, choices=PIZZA_TYPE)
    pizzaSize = models.CharField(max_length=1, choices=PIZZA_SIZE)
    isSpecial = models.BooleanField(blank=True, default=False)
    totalTopping = models.IntegerField(default=0)

    # if no topping, pizza is cheese
    pizzaTopping = models.ManyToManyField(Topping, blank=True)
    pizzaPrice = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.pizzaSize}, {self.pizzaType}, {self.pizzaTopping}, {self.pizzaPrice}, {self.isSpecial}"

class CustomerPizza(models.Model):
    REGULAR = 'R'
    SICILIAN = 'S'
    SMALL = 's'
    LARGE = 'l'

    PIZZA_TYPE = (
        (REGULAR, 'regular'),
        (SICILIAN, 'sicilian'),
    )

    PIZZA_SIZE = (
        (SMALL, 'small'),
        (LARGE, 'large')
    )
    pizzaType = models.CharField(max_length=1, choices=PIZZA_TYPE)
    pizzaSize = models.CharField(max_length=1, choices=PIZZA_SIZE)
    isSpecial = models.BooleanField(blank=True, default=False)
    totalTopping = models.IntegerField(default=0)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

    # if no topping, pizza is cheese
    pizzaTopping = models.ManyToManyField(Topping, blank=True)
    pizzaPrice = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.pizzaSize}, {self.pizzaType}, {self.pizzaPrice}, {self.isSpecial}"


class Sub(models.Model):
    SMALL = 's'
    LARGE = 'l'
    SUB_SIZE = (
        (SMALL, 'small'),
        (LARGE, 'large')
    )
    subSize = models.CharField(max_length=1, choices=SUB_SIZE)
    subName = models.CharField(max_length=64)
    subPrice = models.DecimalField(max_digits=4, decimal_places=2)

    subTopping = models.ManyToManyField(Topping, blank=True)
    def __str__(self):
        return f"{self.subSize}, {self.subName}, {self.subPrice}, {self.subTopping}"

# Only for steak + cheese
class CustomerSub(models.Model):
    SMALL = 's'
    LARGE = 'l'
    SUB_SIZE = (
        (SMALL, 'small'),
        (LARGE, 'large')
    )
    subSize = models.CharField(max_length=1, choices=SUB_SIZE)
    subName = models.CharField(max_length=64)
    subPrice = models.DecimalField(max_digits=4, decimal_places=2)

    subTopping = models.ManyToManyField(Topping, blank=True)
    def __str__(self):
        return f"{self.subSize}, {self.subName}, {self.subPrice}, {self.subTopping}"

class Pasta(models.Model):
    pastaName = models.CharField(max_length=64)
    pastaPrice = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.pastaName}, {self.pastaPrice}"

class Salad(models.Model):
    saladName = models.CharField(max_length=64)
    saladPrice = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.saladName}, {self.saladPrice}"

class Platter(models.Model):
    SMALL = 's'
    LARGE = 'l'
    PLATTER_SIZE = (
        (SMALL, 'small'),
        (LARGE, 'large')
    )
    platterSize = models.CharField(max_length=1, choices=PLATTER_SIZE)
    platterName = models.CharField(max_length=64)
    platterPrice = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.platterSize}, {self.platterName}, {self.platterPrice}"

# Implement last
class Cart(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cartOwner')
    totalPrice = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    pizzaOrdered = models.ManyToManyField(Pizza, blank=True)
    subOrdered = models.ManyToManyField(Sub, blank=True)
    pastaOrdered = models.ManyToManyField(Pasta, blank=True)
    saladOrdered = models.ManyToManyField(Salad, blank=True)
    platterOrdered = models.ManyToManyField(Platter, blank=True)
    