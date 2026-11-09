from django.urls import path  # type: ignore

from. import views


urlpatterns = [
    path("", views.contact, name="contact"),
    path("contact.html", views.contact, name="contact_html"),
]
