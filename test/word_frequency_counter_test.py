from unittest import TestCase
from src.word_frequency_counter import WordFrequencyCounter

class TestWordFrequencyCounter(TestCase):

	def empty_string_should_return_0_test(self):
		frequencyCounter = WordFrequencyCounter()
		frequencyCounter.load_from_string('a b c d')
		self.assertEqual(0, frequencyCounter.count(''))

	def finds_one_occurrence_test(self):
		frequencyCounter = WordFrequencyCounter()
		frequencyCounter.load_from_string('a b c d')
		self.assertEqual(1, frequencyCounter.count('a'))