from django.contrib import admin
from django.urls import path
from .views import update_patch_customer, display_customers, register_customer

urlpatterns = [
    path('', register_customer, name='register_customer'),
    path('updateCustomer', update_patch_customer, name='update_Customer'),
    path('displayCustomer', display_customers, name='display_Customers'),
]