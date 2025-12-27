from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet, basename='customer')

urlpatterns = router.urls

# localhost:8000/customer_vw_api/customers/ => GET request calling
# localhost:8000/customer_vw_api/customers/ => POST request calling
# localhost:8000/customer_vw_api/customers/<int:id>/
# localhost:8000/customer_vw_api/customers/<int:id>/


# from django.urls import path
# from .views import CustomerViewSet

# # For /customers/
# customer_list = CustomerViewSet.as_view({
#     'post': 'create',   # POST → create customer
#     'get': 'list',      # GET → list customers
# })

# # For /customers/<id>/
# customer_detail = CustomerViewSet.as_view({
#     'get': 'retrieve',        # GET → single customer
#     'patch': 'partial_update',# PATCH → update customer
#     'delete': 'destroy',      # DELETE → delete customer
# })

# urlpatterns = [
#     path('customers/', customer_list),
#     path('customers/<int:pk>/', customer_detail),
# ]
