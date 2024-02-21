from django.test import TestCase
from invoices.models import Invoice, InvoiceDetail
from datetime import date

class InvoiceModelTestCase(TestCase):
  def setUp(self):
    self.invoice = Invoice.objects.create(date=date.today(), customer_name="Test Customer")

  def test_invoice_creation(self):
    """Test creation of Invoice object"""
    self.assertEqual(self.invoice.customer_name, "Test Customer")

  def test_invoice_str(self):
    """Test string representation of Invoice object"""
    self.assertEqual(str(self.invoice), "Invoice # 1 - Test Customer")

class InvoiceDetailModelTestCase(TestCase):
  def setUp(self):
    self.invoice = Invoice.objects.create(date=date.today(), customer_name="Test Customer")
    self.invoice_detail = InvoiceDetail.objects.create(
      invoice=self.invoice,
      description="Test Description",
      quantity=1,
      unit_price=10.0,
      price=10.0
      )

  def test_invoice_detail_creation(self):
    """Test creation of InvoiceDetail object"""
    self.assertEqual(self.invoice_detail.description, "Test Description")
    self.assertEqual(self.invoice_detail.quantity, 1)

  def test_invoice_detail_str(self):
    """Test string representation of InvoiceDetail object"""
    expected_str = "Detail for Invoice # 1: Test Description"
    self.assertEqual(str(self.invoice_detail), expected_str)
