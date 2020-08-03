from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from django.contrib import messages

from products.models import Product


""" A view to show all cart contents"""


def view_cart(request):

    return render(request, 'cart/cart.html')


""" Add a quantity of the specified product to the shopping cart """


def add_to_cart(request, item_id):

    product = get_object_or_404(Product, pk=item_id)
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
        messages.success(request, f'Added {product.name} to your cart')

    # Overwrite the variable in the session with the updated version.
    request.session['cart'] = cart
    return redirect(redirect_url)


"""Remove the item from the shopping cart"""


def remove_from_cart(request, item_id):
    
    product = get_object_or_404(Product, pk=item_id)
    cart = request.session.get('cart', {})
    
    cart.pop(item_id)
    messages.success(request, f'Removed {product.name} from your cart')

    request.session['cart'] = cart
    return HttpResponse(status=200)
