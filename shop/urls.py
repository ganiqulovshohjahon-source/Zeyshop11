from django.urls import path  # type: ignore

from . import views

urlpatterns = [
    path("/", views.home, name="home"),
    path("index.html", views.home, name="index_html"),
    path("about/", views.about, name="about"),
    path("about.html", views.about, name="about_html"),
    path("shop/", views.shop, name="shop"),
    path("shop.html", views.shop, name="shop_html"),
    path("shop-single/", views.shop_single, name="shop_single"),
    path("shop-single.html", views.shop_single, name="shop_single_html"),
    path("ariza/", views.Ariza, name="Ariza"),
]
