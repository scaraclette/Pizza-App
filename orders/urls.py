from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("menu/", views.menu, name="menu"),
    path("pizza/", views.pizza, name="pizza"),
    path("sub/", views.sub, name="sub"),
    path("pasta/", views.pasta, name="pasta"),
    path("salad/", views.salad, name="salad"),
    path("platter/", views.platter, name="platter"),
    path("cart/", views.cart, name="cart"),
]
