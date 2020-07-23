from django.shortcuts import render
from .models import Product


""" A view to show all products """

def all_products(request):
    
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
