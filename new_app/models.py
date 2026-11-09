from django.conf import settings  # pyright: ignore[reportMissingModuleSource]
from django.db import models  # pyright: ignore[reportMissingModuleSource]


class shop(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    category = models.CharField(max_length=255)

class add_product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    category = models.CharField(max_length=255)


class Ariza(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    full_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
