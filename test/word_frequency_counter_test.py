from unittest import TestCase
from src.word_frequency_counter import WordFrequencyCounter

class TestWordFrequencyCounter(TestCase):

	simple_test_string = 'a b c d'

	def setUp(self):
		self.frequencyCounter = WordFrequencyCounter()

	def empty_string_should_return_0_test(self):
		self.frequencyCounter.load_from_string('a b c d')
		self.assertEqual(0, self.frequencyCounter.count(''))

	def finds_one_occurrence_test(self):
		self.frequencyCounter.load_from_string('a b c d')
		self.assertEqual(1, self.frequencyCounter.count('a'))

	def finds_zero_occurrences_if_word_not_found_test(self):
		self.frequencyCounter.load_from_string('a b c d')
		self.assertEqual(0, self.frequencyCounter.count('e'))

	def finds_two_occurrences_test(self):
		self.frequencyCounter.load_from_string('a a b c d')
		self.assertEqual(2, self.frequencyCounter.count('a'))

	def summary_should_return_all_frequencies_test(self):
		self.frequencyCounter.load_from_string('a a a a b b b c c d')
		summary = self.frequencyCounter.summary()
		self.assertEqual(4, summary['a'])
		self.assertEqual(3, summary['b'])
		self.assertEqual(2, summary['c'])
		self.assertEqual(1, summary['d'])