from django.contrib import admin
from django.urls import path
from .views import RegisterCustomerView, DisplayCustomerView, UpdateCustomerPatchView, DeleteCustomerView

urlpatterns = [
    path('register/',RegisterCustomerView.as_view(),name='register-customer'),
    path('display/', DisplayCustomerView.as_view(), name='display-customer'),
    path('updatePatch/<int:pk>', UpdateCustomerPatchView.as_view(),name='updatePatch-customer'),
    path('delete/<int:pk/', DeleteCustomerView.as_view(), name='delete-customer')
]