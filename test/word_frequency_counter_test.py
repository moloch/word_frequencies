from unittest import TestCase

class TestWordFrequencyCounter(TestCase):

	def empty_string_should_return_0_test(self):
		frequencyCounter = WordFrequencyCounter()
		frequencyCounter.load_from_string('a b c d')
		self.assertEqual(0, frequencyCounter.count(''))