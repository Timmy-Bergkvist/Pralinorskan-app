from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product, Category
from django.db.models.functions import Lower

def all_products(request):
    """ A view to show all products, including sorting.
        Pagination included for more than 8 products on page.
    """

    product_list = Product.objects.all()

    categories = None
    sort = None
    direction = None
    collection_page = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                product_list = product_list.annotate(lower_name=Lower('name'))

            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            product_list = product_list.order_by(sortkey)

        if 'category' in request.GET:
                categories = request.GET['category'].split(',')
                product_list = Product.objects.filter(category__name__in=categories)
                categories = Category.objects.filter(name__in=categories)
                collection_page = request.GET['category']

    current_sorting = f'{sort}_{direction}'
    # Creates pagination
    page = request.GET.get('page')
    paginator = Paginator(product_list, 8)  # Show 8 products per page

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        'products': products,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'collection_page': collection_page,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
