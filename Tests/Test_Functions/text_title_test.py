import unittest
from text_title import textTitle

class TextTitleTest(unittest.TestCase):
	def test_title(self):
		self.assertEqual(textTitle("salom dunyo"), "Salom Dunyo")
		self.assertEqual(textTitle(''), "Matn bo'sh")

if __name__ == '__main__':
	unittest.main()