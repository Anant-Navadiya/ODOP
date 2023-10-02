from .models import Customer
from .serializers import CustomerSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser


# list of customers
class CustomerListAPIView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUser]

customer_list_view = CustomerListAPIView.as_view()


# create customer
class CustomerCreateAPIView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


customer_create_view = CustomerCreateAPIView.as_view()


# retrieve customer
class CustomerRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


customer_retrieve_view = CustomerRetrieveAPIView.as_view()


# update customer
class CustomerUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


customer_update_view = CustomerUpdateAPIView.as_view()


# destroy customer
class CustomerDestroyAPIView(generics.DestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


customer_destroy_view = CustomerDestroyAPIView.as_view()
