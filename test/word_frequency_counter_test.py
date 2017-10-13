from unittest import TestCase
from src.word_frequency_counter import WordFrequencyCounter
import os

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

	def loads_file_test(self):
		dir_path = os.path.dirname(os.path.realpath(__file__))
		self.frequencyCounter.load_from_file(dir_path + '/test_files/words_000.txt')
		summary = self.frequencyCounter.summary()
		self.assertEqual(2, summary['It'])
		self.assertEqual(2, summary['should'])
		self.assertEqual(1, summary['work'])
		self.assertEqual(1, summary['well'])
		self.assertEqual(1, summary['also'])
		self.assertEqual(1, summary['be'])
		self.assertEqual(1, summary['tested'])
