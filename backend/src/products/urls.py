from django.urls import path, include

from .views import ProductsList, ProductDetail,CategoryDetail

app_name = "products"
urlpatterns = [
    path('products/', ProductsList.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/', ProductDetail.as_view()),
    path('products/<slug:category_slug>/', CategoryDetail.as_view()),
]
