from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from django.contrib import messages

from products.models import Product


""" A view to show all cart contents"""


def view_cart(request):

    return render(request, 'cart/cart.html')


""" Add a quantity of the specified product to the shopping cart """


def add_to_cart(request, item_id):

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    # Gets the cart variable if it exists-
    #  in the session or create it if it doesn't.
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        # Update the quantity if it already exists.
        cart[item_id] += quantity
    else:
        # Add the item to the cart.
        cart[item_id] = quantity

    # Overwrite the variable in the session with the updated version.
    request.session['cart'] = cart
    return redirect(redirect_url)
