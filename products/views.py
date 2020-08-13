from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product, Category


""" A view to show all products """

def all_products(request):
    
    product_list = Product.objects.all()
    # Creates pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(product_list, 12) # Show 12 products per page
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
        
    categories = None
    if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = product_list.filter(category__name__in=categories)
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