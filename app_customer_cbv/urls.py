from django.contrib import admin
from django.urls import path
from .views import RegisterCustomerView, DisplayCustomerView

urlpatterns = [
    path('register/',RegisterCustomerView.as_view(),name='register-customer'),
    path('display/', DisplayCustomerView.as_view(), name='display-customer'),
]