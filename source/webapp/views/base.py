from django.shortcuts import render
from webapp.models import Product


def index_view(request):
        products = Product.objects.all()
        context = {
            'products': products
        }
        return render(request, 'index.html',context)