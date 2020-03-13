# Execute in django shell
from orders.models import *

# TOPPINGS
toppings = ['Pepperoni', 'Sausage', 'Mushrooms', 'Onions', 'Ham', 'Canadian Bacon', 'Pineapple', 'Tomato & Basil', 'Green Peppers', 'Hamburger', 'Spinach', 'Artichoke', 'Buffalo Chicken', 'Barbecue Chicken', 'Anchovies', 'Black Olives', 'Fresh Garlic', 'Zucchini']

for top in toppings:
    u = Toppings(topping=top)
    u.save()
    
# PLATTERS
platter = [
    {'name':'Garden Salad', 'size':'s', 'price':40.00},
    {'name':'Garden Salad', 'size':'l', 'price':65.00},
    {'name':'Greek Salad', 'size':'s', 'price':50.00},
    {'name':'Greek Salad', 'size':'l', 'price':75.00},
    {'name':'Antipasto', 'size':'s', 'price':50.00},
    {'name':'Antipasto', 'size':'l', 'price':75.00},
    {'name':'Baked Ziti', 'size':'s', 'price':40.00},
    {'name':'Baked Ziti', 'size':'l', 'price':65.00},
    {'name':'Meatball Parm', 'size':'s', 'price':50.00},
    {'name':'Meatball Parm', 'size':'l', 'price':75.00},
    {'name':'Chicken Parm', 'size':'s', 'price':55.00},
    {'name':'Chicken Parm', 'size':'l', 'price':85.00},    
    ]

for p in platter:
    platterName = p.get('name')
    platterSize = p.get('size')
    platterPrice = p.get('price')
    new = Platter(platterName=platterName, platterSize=platterSize, platterPrice=platterPrice)
    new.save()

# SALADS
salad = [
    {'name':'Garden Salad', 'price':6.25},
    {'name':'Greek Salad', 'price':8.25},
    {'name':'Antipasto', 'price':8.25},
    {'name':'Salad w/Tuna', 'price':8.25},
]

for s in salad:
    saladName = s.get('name')
    saladPrice = s.get('price')
    new = Salad(saladName=saladName, saladPrice=saladPrice)
    new.save()

# PASTA
pasta = [
    {'name':'Baked Ziti w/ Mozzarella', 'price':6.50},
    {'name':'Baked Ziti w/ Meatballs', 'price':8.75},
    {'name':'Baked Ziti w/ Chicken', 'price':9.75},
]

for p in pasta:
    pastaName = p.get('name')
    pastaPrice = p.get('price')
    new = Pasta(pastaName=pastaName, pastaPrice=pastaPrice)
    new.save()

# SUBS
# Only steak + cheese will be able to have added topping
# TODO handle susage, peppers, & onions with JS to only allow large
sub = [
    {'name':'Cheese', 'size':'s', 'price':6.50},
    {'name':'Italian', 'size':'s', 'price':6.50},
    {'name':'Ham + Cheese', 'size':'s', 'price':6.50},
    {'name':'Meatball', 'size':'s', 'price':6.50},
    {'name':'Tuna', 'size':'s', 'price':6.50},
    {'name':'Turkey', 'size':'s', 'price':7.50},
    {'name':'Chicken Parmigiana', 'size':'s', 'price':7.50},
    {'name':'Eggplant Parmigiana', 'size':'s', 'price':6.50},
    {'name':'Steak', 'size':'s', 'price':6.50},
    {'name':'Steak + Cheese', 'size':'s', 'price':6.95},
    {'name':'Hamburger', 'size':'s', 'price':4.60},
    {'name':'Cheeseburger', 'size':'s', 'price':5.10},
    {'name':'Fried Chicken', 'size':'s', 'price':6.95},
    {'name':'Veggie', 'size':'s', 'price':6.95},
    {'name':'Cheese', 'size':'l', 'price':7.95},
    {'name':'Italian', 'size':'l', 'price':7.95},
    {'name':'Ham + Cheese', 'size':'l', 'price':7.95},
    {'name':'Meatball', 'size':'l', 'price':7.95},
    {'name':'Tuna', 'size':'l', 'price':7.95},
    {'name':'Turkey', 'size':'l', 'price':8.50},
    {'name':'Chicken Parmigiana', 'size':'l', 'price':8.50},
    {'name':'Eggplant Parmigiana', 'size':'l', 'price':7.95},
    {'name':'Steak', 'size':'l', 'price':7.95},
    {'name':'Steak + Cheese', 'size':'l', 'price':8.50},
    {'name':'Sausage, Peppers & Onions', 'size':'l', 'price':8.50},
    {'name':'Hamburger', 'size':'l', 'price':6.95},
    {'name':'Cheeseburger', 'size':'l', 'price':7.45},
    {'name':'Fried Chicken', 'size':'l', 'price':8.50},
    {'name':'Veggie', 'size':'l', 'price':8.50},
]

for s in sub:
    subSize = s.get('size')
    subName = s.get('name')
    subPrice = s.get('price')
    new = Sub(subName=subName, subPrice=subPrice, subSize=subSize)
    new.save()