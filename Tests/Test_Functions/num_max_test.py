import unittest
from num_max import numMax

class NummaxTest(unittest.TestCase):
    def test_max(self):
        self.assertAlmostEqual(numMax(5, 4, 6.5), 6.5)
        self.assertAlmostEqual(numMax([10, 15, 30.5]), 30.5)

if __name__ == "__main__":
    unittest.main()
