"""
Shopping cart unit testing examples.
"""

import unittest
from unittest.mock import patch

from white_box.class_exercises import Product, ShoppingCart


class TestProduct(unittest.TestCase):
    """
    Product unittest class.
    """

    def setUp(self):
        """
        Creates the product properties.
        """
        self.name = "Laptop"
        self.price = 1500

    def test_product_init(self):
        """
        Checks the product properties.
        """
        product = Product(self.name, self.price)
        self.assertEqual(product.name, self.name)
        self.assertEqual(product.price, self.price)

    @patch("builtins.print")
    def test_view_product(self, mock_print):
        """
        Checks the product display function.
        """
        product = Product(self.name, self.price)
        result = product.view_product()
        expected_msg = f"The product {self.name} has a price of {self.price}"

        self.assertEqual(result, expected_msg)
        mock_print.assert_called_once_with(expected_msg)


class TestShoppingCart(unittest.TestCase):
    """
    ShoppingCart unittest class.
    """

    def test_shopping_cart_init(self):
        """
        Checks the shopping cart initial properties.
        """
        cart = ShoppingCart()
        self.assertEqual(cart.items, [])

    def test_add_product_new_product(self):
        """
        Checks adding a new product to the cart.
        """
        cart = ShoppingCart()
        product = Product("Laptop", 1500)

        cart.add_product(product)

        self.assertEqual(len(cart.items), 1)
        self.assertEqual(cart.items[0]["product"], product)
        self.assertEqual(cart.items[0]["quantity"], 1)

    def test_add_product_existing_product(self):
        """
        Checks adding an existing product increases quantity.
        """
        cart = ShoppingCart()
        product = Product("Laptop", 1500)

        cart.add_product(product, 2)
        cart.add_product(product, 3)

        self.assertEqual(len(cart.items), 1)
        self.assertEqual(cart.items[0]["product"], product)
        self.assertEqual(cart.items[0]["quantity"], 5)

    def test_remove_product_partial_quantity(self):
        """
        Checks removing part of the quantity of a product.
        """
        cart = ShoppingCart()
        product = Product("Laptop", 1500)

        cart.add_product(product, 5)
        cart.remove_product(product, 2)

        self.assertEqual(len(cart.items), 1)
        self.assertEqual(cart.items[0]["quantity"], 3)

    def test_remove_product_complete_quantity(self):
        """
        Checks removing all quantity of a product.
        """
        cart = ShoppingCart()
        product = Product("Laptop", 1500)

        cart.add_product(product, 2)
        cart.remove_product(product, 2)

        self.assertEqual(cart.items, [])

    def test_remove_product_more_than_existing_quantity(self):
        """
        Checks removing more than existing quantity removes the product.
        """
        cart = ShoppingCart()
        product = Product("Laptop", 1500)

        cart.add_product(product, 2)
        cart.remove_product(product, 5)

        self.assertEqual(cart.items, [])

    def test_remove_product_not_in_cart(self):
        """
        Checks removing a product not present in the cart.
        """
        cart = ShoppingCart()
        product1 = Product("Laptop", 1500)
        product2 = Product("Mouse", 50)

        cart.add_product(product1, 2)
        cart.remove_product(product2, 1)

        self.assertEqual(len(cart.items), 1)
        self.assertEqual(cart.items[0]["product"], product1)
        self.assertEqual(cart.items[0]["quantity"], 2)

    @patch("builtins.print")
    def test_view_cart_with_items(self, mock_print):
        """
        Checks displaying the cart with items.
        """
        cart = ShoppingCart()
        product1 = Product("Laptop", 1500)
        product2 = Product("Mouse", 50)

        cart.add_product(product1, 2)
        cart.add_product(product2, 3)

        cart.view_cart()

        self.assertEqual(mock_print.call_count, 2)
        mock_print.assert_any_call("2 x Laptop - $3000")
        mock_print.assert_any_call("3 x Mouse - $150")

    @patch("builtins.print")
    def test_view_cart_empty(self, mock_print):
        """
        Checks displaying an empty cart.
        """
        cart = ShoppingCart()
        cart.view_cart()
        mock_print.assert_not_called()

    @patch("builtins.print")
    def test_checkout_with_items(self, mock_print):
        """
        Checks checkout with products in the cart.
        """
        cart = ShoppingCart()
        product1 = Product("Laptop", 1500)
        product2 = Product("Mouse", 50)

        cart.add_product(product1, 2)
        cart.add_product(product2, 3)

        cart.checkout()

        self.assertEqual(mock_print.call_count, 2)
        mock_print.assert_any_call("Total: $3150")
        mock_print.assert_any_call("Checkout completed. Thank you for shopping!")

    @patch("builtins.print")
    def test_checkout_empty_cart(self, mock_print):
        """
        Checks checkout with an empty cart.
        """
        cart = ShoppingCart()
        cart.checkout()

        self.assertEqual(mock_print.call_count, 2)
        mock_print.assert_any_call("Total: $0")
        mock_print.assert_any_call("Checkout completed. Thank you for shopping!")
