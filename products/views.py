from django.shortcuts import render, get_object_or_404
from .models import Product


""" A view to show all products """

def all_products(request):
    
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)



""" A view to show individual product details """

def product_detail(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)