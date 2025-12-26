from django.contrib import admin
from django.urls import path
from .views import RegisterCustomerView, DisplayCustomerView, UpdateCustomerPatchView

urlpatterns = [
    path('register/',RegisterCustomerView.as_view(),name='register-customer'),
    path('display/', DisplayCustomerView.as_view(), name='display-customer'),
    path('updatePatch/<int:pk>', UpdateCustomerPatchView.as_view(),name='updatePatch-customer'),
]