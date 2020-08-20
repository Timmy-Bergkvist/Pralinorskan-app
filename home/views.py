from django.shortcuts import render
from products.models import Product, Category


def index(request):
    '''
    A view of the index/home page that displays
    four of the sites best selling products.
    '''

    products = Product.objects.all()
    bestsellers = products.filter(pk__in=[9,23,10,13])

    context = {
        'bestsellers': bestsellers,
    }
    
    template = 'home/index.html'

    
    return render(request, template, context)
