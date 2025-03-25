import unittest
from src.controller import greet

class TestMainFunction(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Alice"), "Hello, Alice! Welcome to PythonDemoApp 🚀")

if __name__ == '__main__':
    unittest.main()
