from unittest import TestCase
from src.loaders import StringLoader, FileLoader
import os

class TestStringLoader(TestCase):

	def should_load_string_into_lowercase_words_list_test(self):
		stringLoader = StringLoader()
		words_list = stringLoader.load('I am a String.\n')
		self.assertEqual(['i', 'am', 'a', 'string'], words_list)

class TestFileLoader(TestCase):

	def should_load_file_into_lowercase_words_list_test(self):
		dir_path = os.path.dirname(os.path.realpath(__file__))
		words_list = FileLoader().load(dir_path + '/test_files/words_000.txt')
		self.assertEqual(['it', 'should', 'work', 'well', 'it', 'should', 'also', 'be', 'tested'], words_list)
