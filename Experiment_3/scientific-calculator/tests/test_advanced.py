import unittest
from advanced_operations import square_root, power

class TestAdvancedOperations(unittest.TestCase):
    def test_sqaure_root(self):
        self.assertEqual(square_root(16), 4)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)


if __name__ == '__main__':
    unittest.main()
              
