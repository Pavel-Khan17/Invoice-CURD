from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from invoices.models import Invoice, InvoiceDetail
from datetime import date

INVOICE_DETIAL_URL = reverse('invoices:invoice-detail-list')

def invoice_detail_url(invoice_detail_id):
  """ Return invoice details url """
  return reverse('invoices:invoice-detail-detail', args=[invoice_detail_id])

class InvoiceDetailAPITestCase(TestCase):
  
  def setUp(self):
    self.client = APIClient()
    self.invoice = Invoice.objects.create(date=date.today(), customer_name="Test Customer")
    self.invoice_detail_data = {
      'invoice': self.invoice,
      'description': 'Test Description',
      'quantity': 1,
      'unit_price': 10.0,
      'price': 10.0
    }
    self.invoice_detail = InvoiceDetail.objects.create(**self.invoice_detail_data)

  def test_create_invoice_detail(self):
    response = self.client.post(INVOICE_DETIAL_URL, self.invoice_detail_data)
    self.assertEqual(InvoiceDetail.objects.count(), 1)

  def test_get_invoice_detail_list(self):
    response = self.client.get(INVOICE_DETIAL_URL)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 1)

  def test_get_invoice_detail_detail(self):
    url = invoice_detail_url(self.invoice_detail.id)
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_update_invoice_detail(self):
    url = invoice_detail_url(self.invoice_detail.id)
    updated_data = {
      'description': 'Updated Description',
      'quantity': 2
    }
    response = self.client.patch(url, updated_data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.invoice_detail.refresh_from_db()
    self.assertEqual(self.invoice_detail.description, 'Updated Description')
    self.assertEqual(self.invoice_detail.quantity, 2)

  def test_delete_invoice_detail(self):
    url = invoice_detail_url(self.invoice_detail.id)
    response = self.client.delete(url)
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    self.assertEqual(InvoiceDetail.objects.count(), 0)
