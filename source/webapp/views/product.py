from webapp.models import Product
from django.shortcuts import render, redirect, get_object_or_404
from webapp.forms import ProductForm

def product_create_view(request, *args, **kwargs):
    form = ProductForm()
    if request.method == 'GET':
        return render(request, 'create.html', context={'form': form})
    form = ProductForm(request.POST)
    if not form.is_valid():    
        return render(request, 'create.html', context={'form': form})
    product = Product.objects.create(**form.cleaned_data)        
    if request.method =='POST':
        return redirect('index')
