from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ContactMessageForm


def contact(request):
    if request.method == "POST":
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you. Your message has been sent.")
            return redirect("contact")
    else:
        form = ContactMessageForm()

    return render(request, "contact.html", {"form": form})
