from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("customer/", include("app_customer.urls")), # function base view

    path("customer_cbv/", include("app_customer_cbv.urls")),

    path("customer_vw_api/", include("app_customer_cbvAPI.urls")),
]