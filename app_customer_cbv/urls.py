from django.contrib import admin
from django.urls import path
from .views import RegisterCustomerView, DisplayCustomerView, UpdateCustomerPatchView, DeleteCustomerView, UpdateCustomerPutView, DeleteCustomerViewUrl

urlpatterns = [
    path('register/',RegisterCustomerView.as_view(),name='register-customer'),
    path('display/', DisplayCustomerView.as_view(), name='display-customer'),
    path('updatePatch/<int:pk>/', UpdateCustomerPatchView.as_view(),name='updatePatch-customer'),
    path('delete_apiURL/<int:pk>/', DeleteCustomerViewUrl.as_view(), name='delete-customer'),
    path('delete_api/', DeleteCustomerView.as_view(), name='delete-customer'),
    path('updatePut/<int:pk>/', UpdateCustomerPutView.as_view(),name='updatePut-customer'),
]
