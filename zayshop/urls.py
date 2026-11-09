from django.conf import settings  # pyright: ignore[reportMissingModuleSource]
from django.contrib import admin  # pyright: ignore[reportMissingModuleSource]
from django.urls import include, path, re_path  # pyright: ignore[reportMissingModuleSource]
from django.views.generic import TemplateView  # pyright: ignore[reportMissingModuleSource]
from django.views.static import serve  # pyright: ignore[reportMissingModuleSource]
from shop import views as shop_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("contact/", TemplateView.as_view(template_name="contact.html"), name="contact"),
    path("", TemplateView.as_view(template_name="index.html"), name="home"),
    path("about/", TemplateView.as_view(template_name="about.html"), name="about"),
    path("shop/", shop_views.shop, name="shop"),
    path("shop-single/", TemplateView.as_view(template_name="shop-single.html"), name="shop_single"),
    path("", include("new_app.urls")),
    re_path(r"^assets/(?P<path>.*)$", serve, {"document_root": settings.BASE_DIR / "assets"}),
    path("ariza/", shop_views.Ariza, name="ariza"),
    path("log-in/", shop_views.Log_in, name="log_in"),]
