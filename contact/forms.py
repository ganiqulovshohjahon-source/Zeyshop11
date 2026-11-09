from django import forms  # type: ignore[reportMissingModuleSource]

from .models import ContactMessage


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "subject", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control mt-1", "placeholder": "Name", "autocomplete": "name"}),
            "email": forms.EmailInput(attrs={"class": "form-control mt-1", "placeholder": "Email", "autocomplete": "email"}),
            "subject": forms.TextInput(attrs={"class": "form-control mt-1", "placeholder": "Subject"}),
            "message": forms.Textarea(attrs={"class": "form-control mt-1", "placeholder": "Message", "rows": 8}),
        }
