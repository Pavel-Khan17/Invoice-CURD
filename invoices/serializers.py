from rest_framework import serializers
from .models import Invoice, InvoiceDetail

class InvoiceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Invoice
    fields = ['id', 'date', 'customer_name']


class InvoiceDetailSerializer(serializers.ModelSerializer):
  class Meta:
    model = InvoiceDetail
    fields = ['id', 'invoice', 'description', 'quantity', 'unit_price', 'price']
