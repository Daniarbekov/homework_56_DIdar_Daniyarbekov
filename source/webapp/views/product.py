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


def product_detail_view(request,pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'detail.html', context={'product': product})

def product_update_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        form = ProductForm(initial={
            'name': product.name, 
            'category': product.category,
            'price': product.price,
            'description':product.description,
            'image': product.image,
            'balance': product.balance
        })
        return render(request, 'update.html', context={'form': form})
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.name = form.cleaned_data['name']
            product.category = form.cleaned_data['category']
            product.price = form.cleaned_data['price']
            product.description = form.cleaned_data['description']
            product.image = form.cleaned_data['image']
            product.balance = form.cleaned_data['balance']
            product.save()
            return redirect('detail', pk=product.pk)
        else:
            return render(request, 'update.html', context={'form': form, 'product': product})
        
def product_delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
       return render(request, 'delete.html', context={'product': product})
    elif request.method == 'POST':
        product.delete()
        return redirect('index')