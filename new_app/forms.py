from django.forms import ModelForm  # type: ignore
from .models import shop


class shopModelForm(ModelForm):
    class Meta:
        model = shop
        fields = ['name', 'price', 'category']