import unittest
from hello import greet

class TestHello(unittest.TestCase):
    def test_greet(self):
        name = "Jenkins"
        result = greet(name)
        self.assertEqual(result, "Hello, Jenkins!")

if __name__ == "__main__":
    unittest.main()