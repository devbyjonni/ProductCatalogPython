import unittest
from decimal import Decimal
from unittest.mock import patch

from src.controller.catalog_controller import ProductCatalogController


class TestProductCatalogController(unittest.TestCase):

    def setUp(self):
        self.controller = ProductCatalogController()

    @patch("builtins.input", return_value="  Electronics  ")
    def test_get_user_input_returns_trimmed_string(self, mock_input):
        result = self.controller.get_user_input("Enter a Category: ")
        self.assertEqual(result, "Electronics")

    @patch("builtins.input", return_value="Q")
    def test_get_user_input_returns_none_on_quit(self, mock_input):
        result = self.controller.get_user_input("Enter a Category: ")
        self.assertIsNone(result)

    @patch("builtins.input", return_value="199.99")
    def test_read_valid_price_returns_decimal(self, mock_input):
        result = self.controller.read_valid_price("Enter a Price: ")
        self.assertEqual(result, Decimal("199.99"))

    @patch("builtins.input", return_value="Q")
    def test_read_valid_price_returns_none_on_quit(self, mock_input):
        result = self.controller.read_valid_price("Enter a Price: ")
        self.assertIsNone(result)

    def test_valid_price_parsing(self):
        valid_inputs = [("100", True), ("0", False), ("-10", False), ("abc", False)]
        for input_str, expected in valid_inputs:
            try:
                price = Decimal(input_str)
                is_valid = price > 0
            except:
                is_valid = False
            self.assertEqual(is_valid, expected)


if __name__ == "__main__":
    unittest.main()
