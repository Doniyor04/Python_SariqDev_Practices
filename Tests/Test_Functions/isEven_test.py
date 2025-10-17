import unittest
from isEven import isEven

class IsEvenTest(unittest.TestCase):
	def test_even(self):
		list_test = range(1, 11)
		self.assertAlmostEqual(isEven(list_test), [2, 4, 6, 8, 10])
		self.assertAlmostEqual(isEven([]), "Ro'yxat bo'sh")

if __name__ == '__main__':
	unittest.main()
