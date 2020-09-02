from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm, UserDeleteForm
from django.contrib.auth.models import User

from checkout.models import Order


@login_required
def profile(request):

    """ Display the user's profile. """

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def orders(request):

    """ Display the user's orders. """

    profile = get_object_or_404(UserProfile, user=request.user)

    orders = profile.orders.all()
    template = 'profiles/orders.html'
    context = {
        'orders': orders,
        'on_orders_page': True
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):

    """ Getting the checkout_success order history """

    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_orders': True,
    }

    return render(request, template, context)


@login_required
def delete_account(request):
    """ Allow user to delete their account """

    if request.method == 'POST':
        delete_form = UserDeleteForm(request.POST, instance=request.user)
        if delete_form.is_valid():
            user = request.user
            user.delete()
            messages.info(request, 'Your account has been deleted.')
            return redirect('home')
    else:
        delete_form = UserDeleteForm(instance=request.user)

    return render(request, 'delete_account.html', {'delete_form': delete_form})
