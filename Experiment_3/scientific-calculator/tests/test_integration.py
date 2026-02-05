import unittest
from basic_operations import add
from advanced_operations import sine

class TestIntegration(unittest.TestCase):
    def test_combined_operations(self):
        result = add(10, sine(30))
        self.assertAlmostEqual(result, 10.5, places=1)


if __name__ == '__main__':
    unittest.main()
