# test_Requirements-PM.md

import unittest
from unittest.mock import patch, MagicMock
from backend.order import place_order, OrderStatus, generate_invoice, email_invoice

class TestCheckoutAndPayment(unittest.TestCase):
  """
  Test suite for checkout and payment process, focusing on payment gateway integration.
  """

  @patch('backend.order.check_stock_availability')
  @patch('backend.order.payment_gateway.charge')
  @patch('backend.order.generate_invoice')
  @patch('backend.order.email_invoice')
  def test_successful_payment_flow(self, mock_email_invoice, mock_generate_invoice, mock_charge, mock_check_stock):
    """
    Test successful payment scenario:
    - Stock is available
    - Payment gateway returns success
    - Invoice is generated and emailed
    - Order status is updated to 'processing'
    """
    mock_check_stock.return_value = True
    mock_charge.return_value = {'status': 'success', 'transaction_id': 'abc123'}
    mock_generate_invoice.return_value = 'invoice.pdf'
    mock_email_invoice.return_value = True

    order_data = {
      'user_id': 1,
      'cart_items': [{'book_id': 101, 'quantity': 2}],
      'shipping_address': '123 Main St',
      'payment_method': 'credit_card'
    }

    result = place_order(order_data)

    self.assertEqual(result['status'], OrderStatus.PROCESSING)
    mock_check_stock.assert_called_once()
    mock_charge.assert_called_once()
    mock_generate_invoice.assert_called_once()
    mock_email_invoice.assert_called_once()

  @patch('backend.order.check_stock_availability')
  @patch('backend.order.payment_gateway.charge')
  def test_failed_payment_flow(self, mock_charge, mock_check_stock):
    """
    Test failed payment scenario:
    - Stock is available
    - Payment gateway returns failure
    - Invoice is not generated or emailed
    - Order status is updated to 'pending' or 'cancelled'
    """
    mock_check_stock.return_value = True
    mock_charge.return_value = {'status': 'failure', 'error': 'Card declined'}

    order_data = {
      'user_id': 2,
      'cart_items': [{'book_id': 102, 'quantity': 1}],
      'shipping_address': '456 Elm St',
      'payment_method': 'paypal'
    }
    with patch('backend.order.generate_invoice') as mock_generate_invoice, \
       patch('backend.order.email_invoice') as mock_email_invoice:
      result = place_order(order_data)

      self.assertIn(result['status'], [OrderStatus.PENDING, OrderStatus.CANCELLED])
      mock_check_stock.assert_called_once()
      mock_charge.assert_called_once()
      mock_generate_invoice.assert_not_called()
      mock_email_invoice.assert_not_called()

    @patch('backend.order.check_stock_availability')
    def test_out_of_stock(self, mock_check_stock):
      """
      Test order placement when stock is insufficient:
      - Stock check fails
      - Payment gateway is not called
      - Order is not processed
      """
      mock_check_stock.return_value = False

      order_data = {
        'user_id': 3,
        'cart_items': [{'book_id': 103, 'quantity': 10}],
        'shipping_address': '789 Oak St',
        'payment_method': 'credit_card'
      }

      with patch('backend.order.payment_gateway.charge') as mock_charge:
        result = place_order(order_data)
        self.assertEqual(result['status'], OrderStatus.CANCELLED)
        mock_check_stock.assert_called_once()
        mock_charge.assert_not_called()

    @patch('backend.order.check_stock_availability')
    @patch('backend.order.payment_gateway.charge')
    def test_invalid_payment_method(self, mock_charge, mock_check_stock):
      """
      Test order placement with an unsupported payment method:
      - Stock is available
      - Payment gateway is not called
      - Order is not processed
      """
      mock_check_stock.return_value = True

      order_data = {
        'user_id': 4,
        'cart_items': [{'book_id': 104, 'quantity': 1}],
        'shipping_address': '321 Maple Ave',
        'payment_method': 'bitcoin'  # unsupported
      }

      with patch('backend.order.generate_invoice') as mock_generate_invoice, \
         patch('backend.order.email_invoice') as mock_email_invoice:
        result = place_order(order_data)
        self.assertEqual(result['status'], OrderStatus.CANCELLED)
        mock_check_stock.assert_called_once()
        mock_charge.assert_not_called()
        mock_generate_invoice.assert_not_called()
        mock_email_invoice.assert_not_called()

    @patch('backend.order.check_stock_availability')
    @patch('backend.order.payment_gateway.charge')
    def test_payment_gateway_timeout(self, mock_charge, mock_check_stock):
      """
      Test order placement when payment gateway times out:
      - Stock is available
      - Payment gateway raises a timeout exception
      - Order is not processed
      """
      mock_check_stock.return_value = True
      mock_charge.side_effect = TimeoutError("Payment gateway timeout")

      order_data = {
        'user_id': 5,
        'cart_items': [{'book_id': 105, 'quantity': 1}],
        'shipping_address': '555 Pine St',
        'payment_method': 'credit_card'
      }

      with patch('backend.order.generate_invoice') as mock_generate_invoice, \
         patch('backend.order.email_invoice') as mock_email_invoice:
        result = place_order(order_data)
        self.assertEqual(result['status'], OrderStatus.PENDING)
        mock_check_stock.assert_called_once()
        mock_charge.assert_called_once()
        mock_generate_invoice.assert_not_called()
        mock_email_invoice.assert_not_called()

    @patch('backend.order.check_stock_availability')
    @patch('backend.order.payment_gateway.charge')
    @patch('backend.order.generate_invoice')
    @patch('backend.order.email_invoice')
    def test_invoice_email_failure(self, mock_email_invoice, mock_generate_invoice, mock_charge, mock_check_stock):
      """
      Test order placement when invoice email fails:
      - Stock is available
      - Payment is successful
      - Invoice is generated but email sending fails
      - Order status is still processing, but error is logged/handled
      """
      mock_check_stock.return_value = True
      mock_charge.return_value = {'status': 'success', 'transaction_id': 'xyz789'}
      mock_generate_invoice.return_value = 'invoice2.pdf'
      mock_email_invoice.return_value = False  # Simulate email failure

      order_data = {
        'user_id': 6,
        'cart_items': [{'book_id': 106, 'quantity': 1}],
        'shipping_address': '777 Cedar Rd',
        'payment_method': 'paypal'
      }

      result = place_order(order_data)
      self.assertEqual(result['status'], OrderStatus.PROCESSING)
      mock_check_stock.assert_called_once()
      mock_charge.assert_called_once()
      mock_generate_invoice.assert_called_once()
      mock_email_invoice.assert_called_once()
      mock_check_stock.assert_called_once()
      mock_charge.assert_not_called()

if __name__ == '__main__':
  unittest.main()