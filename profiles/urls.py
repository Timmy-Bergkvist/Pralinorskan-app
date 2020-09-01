from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('orders/', views.orders, name='orders'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('account_delete/', views.delete_account, name="delete_account"),
]