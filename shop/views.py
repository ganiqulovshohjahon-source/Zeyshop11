# pyright: reportMissingModuleSource=false
import django.shortcuts
from new_app.models import shop as Product


def home(request):
    return django.shortcuts.render(request, "index.html")


def about(request):
    return django.shortcuts.render(request, "about.html")


def shop(request):
    products = Product.objects.order_by("-id")
    return django.shortcuts.render(request, "shop.html", {"products": products})


def shop_single(request):
    return django.shortcuts.render(request, "shop-single.html")

def Ariza(request):
    return django.shortcuts.render(request, "Ariza.html")    

def Log_in(request):
    return django.shortcuts.render(request, "log in.html")