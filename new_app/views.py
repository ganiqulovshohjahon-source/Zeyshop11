from django.shortcuts import redirect, render
from .forms import shopModelForm

def add_product(request):
    if request.method == 'POST':
        form = shopModelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("shop")
    else:
        form = shopModelForm()

    return render(request, 'add_coffe.html', context={'form': form})