from django.urls import path
from .views import CustomerViewSet

# For /customers/
customer_list = CustomerViewSet.as_view({
    'post': 'create',   # POST → create customer
    'get': 'list',      # GET → list customers
})

# For /customers/<id>/
customer_detail = CustomerViewSet.as_view({
    'get': 'retrieve',        # GET → single customer
    'patch': 'partial_update',# PATCH → update customer
    'delete': 'destroy',      # DELETE → delete customer
})

urlpatterns = [
    path('customers/', customer_list),
    path('customers/<int:pk>/', customer_detail),
]
