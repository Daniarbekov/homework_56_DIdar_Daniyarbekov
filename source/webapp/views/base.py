from django.shortcuts import render
from webapp.models import Product


def index_view(request):
        products = Product.objects.filter(balance__gte=1)
        context = {
            'products': products
        }
        return render(request, 'index.html',context)