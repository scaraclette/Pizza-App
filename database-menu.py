# Execute in django shell
from orders.models import *

toppings = ['Pepperoni', 'Sausage', 'Mushrooms', 'Onions', 'Ham', 'Canadian Bacon', 'Pineapple', 'Tomato & Basil', 'Green Peppers', 'Hamburger', 'Spinach', 'Artichoke', 'Buffalo Chicken', 'Barbecue Chicken', 'Anchovies', 'Black Olives', 'Fresh Garlic', 'Zucchini']

for top in toppings:
    u = Toppings(topping=top)
    u.save()
    