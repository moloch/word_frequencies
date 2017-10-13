from unittest import TestCase
from src.word_frequency_counter import WordFrequencyCounter
from src.loaders import StringLoader, FileLoader
import os

class TestWordFrequencyCounter(TestCase):

	def setUp(self):
		words_list = ['it', 'should', 'work', 'well', 'it', 'should', 'also', 'be', 'tested']
		self.frequencyCounter = WordFrequencyCounter(words_list)

	def summary_test(self):
		summary = self.frequencyCounter.summary()
		self.assertEqual(2, summary['it'])
		self.assertEqual(2, summary['should'])
		self.assertEqual(1, summary['work'])
		self.assertEqual(1, summary['well'])
		self.assertEqual(1, summary['also'])
		self.assertEqual(1, summary['be'])
		self.assertEqual(1, summary['tested'])

	def textual_summary_test(self):
		textual_summary = self.frequencyCounter.textual_summary()
		self.assertEqual('- it: 2\n- should: 2\n- also: 1\n- be: 1\n- tested: 1\n- well: 1\n- work: 1\n', textual_summary)