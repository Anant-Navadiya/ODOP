from django.urls import include, path


app_name = "api"
urlpatterns = [
    path("customers/", include("src.customers.urls", namespace="customers")),
]