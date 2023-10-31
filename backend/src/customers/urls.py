# from django.urls import include, path
# from .views import (customer_list_view,customer_create_view,customer_retrieve_view,customer_update_view,customer_destroy_view)
#
app_name = "customer"
#
# urlpatterns = [
#   path('', customer_list_view, name="customer.list"),
#   path('create/', customer_create_view, name="customer.create"),
#   path('<slug:pk>/', customer_retrieve_view, name="customer.retrieve"),
#   path('<slug:pk>/update/', customer_update_view, name="customer.update"),
#   path('<slug:pk>/destroy/', customer_destroy_view, name="customer.destroy")
# ]

from .views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', UserViewSet, basename='customer')
urlpatterns = router.urls