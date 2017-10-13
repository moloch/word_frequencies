from unittest import TestCase
from src.word_frequency_counter import WordFrequencyCounter

class TestWordFrequencyCounter(TestCase):

	def setUp(self):
		self.frequencyCounter = WordFrequencyCounter()

	def summary_should_return_all_frequencies_test(self):
		self.frequencyCounter.load_from_string('a a a a b b b c c d')
		summary = self.frequencyCounter.summary()
		self.assertEqual(4, summary['a'])
		self.assertEqual(3, summary['b'])
		self.assertEqual(2, summary['c'])
		self.assertEqual(1, summary['d'])