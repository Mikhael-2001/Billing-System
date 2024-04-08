from django.urls import path, include
from billing.views import *

urlpatterns = [
    path('api/employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('api/employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),

    path('api/products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('api/products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),

    path('api/customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('api/customers/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),

    path('api/bills/', BillListCreateView.as_view(), name='bill-list-create'),
    path('api/bills/<int:pk>/', BillDetailView.as_view(), name='bill-detail'),
]
