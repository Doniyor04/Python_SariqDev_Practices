import unittest
from finobachchi import finobachchi

class FinobachchiTest(unittest.TestCase):
    def test_finobachchi(self):
        self.assertAlmostEqual(finobachchi(100, 34), True)
        self.assertAlmostEqual(finobachchi(100, 35), False)
        self.assertAlmostEqual(finobachchi(0), False)

if __name__ == "__main__":
    unittest.main()
