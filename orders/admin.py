from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Topping)
admin.site.register(Pizza)
admin.site.register(CustomerPizza)
admin.site.register(Sub)
admin.site.register(CustomerSub)
admin.site.register(Pasta)
admin.site.register(CustomerPasta)
admin.site.register(Salad)
admin.site.register(CustomerSalad)
admin.site.register(Platter)
admin.site.register(CustomerPlatter)
admin.site.register(Cart)