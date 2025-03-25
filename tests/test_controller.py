import unittest

from src.controller.catalog_controller import greet


class TestController(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Bob"), "Hello, Bob! Welcome to PythonDemoApp 🚀")


if __name__ == "__main__":
    unittest.main()
