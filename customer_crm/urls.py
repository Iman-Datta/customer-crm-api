from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("customer/", include("app_customer.urls")),
    path("customer_cbv/", include("app_customer_cbv.urls")),
]