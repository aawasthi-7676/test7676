import unittest
import cap

class TestCap(unittest.TestCase):
	print('Inside TestCap fun')

	def one_word_text(self):
		print('Inside one_word_text')
		text ='python'
		result = cap.cap_text(text)
		self.assertEqual(result,'Python')

	def two_word_text(self):
		print('Inside two_word_text')
		text ='abhi priya'
		result = cap.cap_text(text)
		self.assertEqual(result,'Abhi Priya')

if __name__ =='__main__':
	print('Inside Main')
	unittest.main()
