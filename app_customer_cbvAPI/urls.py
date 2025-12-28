from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet, basename='customer')

urlpatterns = router.urls

# localhost:8000/customer_vw_api/customers/ => GET request calling
# localhost:8000/customer_vw_api/customers/ => POST request calling
# localhost:8000/customer_vw_api/customers/<int:id>/
# localhost:8000/customer_vw_api/customers/<int:id>/
