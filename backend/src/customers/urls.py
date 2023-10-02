from django.urls import include, path
from .views import (user_list_view)

app_name = "customer"

urlpatterns = [
  path('customer/', user_list_view, name="customer.list")
]