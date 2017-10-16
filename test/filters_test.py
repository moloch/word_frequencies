import os

from unittest import TestCase
from src.filters import FileFilter

class TestFileFilter(TestCase):
	def filter_out_undesired_words_test(self):
		dir_path = os.path.dirname(os.path.realpath(__file__))
		path = dir_path + '/test_files/filter_000.txt'
		fileFilter = FileFilter(path)
		word_list = ['one','two','three','four','five','six','seven','eight', 'nine', 'ten']
		filtered_words = fileFilter.filter(word_list)
		self.assertEqual(['two', 'four', 'six', 'seven', 'eight', 'nine', 'ten'], filtered_words)