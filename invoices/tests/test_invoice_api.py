from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from invoices.models import Invoice, InvoiceDetail
from datetime import date

INVOICE_URL = reverse('invoices:invoice-list')


def invoice_detail_url(invoice_id):
  """ Return invoice details url """
  return reverse('invoices:invoice-detail', args=[invoice_id])

class InvoiceAPITestCase(TestCase):
  """ Test invoice CURD api """
  def setUp(self):
    self.client = APIClient()
    self.invoice_data = {
      'date': date.today(),
      'customer_name': 'Test Customer'
    }
    self.invoice = Invoice.objects.create(**self.invoice_data)


  def test_create_invoice(self):
    """ test that invoice created successfully """
    response = self.client.post(INVOICE_URL, self.invoice_data)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Invoice.objects.count(), 2)

  def test_get_invoice_list(self):
    """ test that invoice list retrieve successfullu """
    response = self.client.get(INVOICE_URL)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 1)

  def test_get_invoice_detail(self):
    """ test that single invoice retrieve successfullu """
    url = invoice_detail_url(self.invoice.id)
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_update_invoice(self):
    """ test that invoice update successfullu """
    url = invoice_detail_url(self.invoice.id)
    updated_data = {
      'date': date.today(),
      'customer_name': 'Updated Customer'
    }
    response = self.client.put(url, updated_data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.invoice.refresh_from_db()
    self.assertEqual(self.invoice.customer_name, 'Updated Customer')

  def test_delete_invoice(self):
    """ test that invoice delete successfullu """
    url = invoice_detail_url(self.invoice.id)
    response = self.client.delete(url)
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    self.assertEqual(Invoice.objects.count(), 0)

