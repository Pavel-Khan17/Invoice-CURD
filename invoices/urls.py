from django.urls import path

app_name = 'invoices'

from .views import (
  InvoiceListCreateAPIView,
  InvoiceRetrieveUpdateDestroyAPIView,
  InvoiceDetailListCreateAPIView,
  InvoiceDetailRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
  path('invoices/', InvoiceListCreateAPIView.as_view(), name='invoice-list'),
  path('invoices/<int:pk>/', InvoiceRetrieveUpdateDestroyAPIView.as_view(), name='invoice-detail'),
  path('invoice_details/', InvoiceDetailListCreateAPIView.as_view(), name='invoice-detail-list'),
  path('invoice_details/<int:pk>/', InvoiceDetailRetrieveUpdateDestroyAPIView.as_view(), name='invoice-detail-detail'),
]