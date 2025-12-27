from django.contrib import admin
from django.urls import path
from .views import update_patch_customer, display_customers, register_customer, delete_customer, update_put_customer

urlpatterns = [
    path('', register_customer, name='register_customer'),
    path('display/', display_customers, name='display_Customers'),
    path('delete/<int:pk>/', delete_customer, name='delete_Customers'),
    path('partial-update/<int:pk>/', update_patch_customer, name='update_Customer'),
    path('all-update/<int:pk>/', update_put_customer, name='update-customer-put'),
]