from django.shortcuts import render, get_object_or_404
from .models import Product, Category



""" A view to show all products """

def all_products(request):
    
    products = Product.objects.all()
    categories = None


    if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    context = {
        'products': products,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)



""" A view to show individual product details """

def product_detail(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)