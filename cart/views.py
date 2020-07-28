from django.shortcuts import render



""" A view to show all cart contents"""

def view_cart(request):
    
    return render(request, 'cart/cart.html')