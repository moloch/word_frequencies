from unittest import TestCase
import subprocess, os

class TestCountWords(TestCase):
	def count_words_command_test(self):
		dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
		filename = dir_path + '/test/test_files/words_000.txt'
		output = subprocess.run(["python", "count_words.py", filename], stdout=subprocess.PIPE).stdout
		expected_output = 'Word frequencies for '+ filename +':\n- it: 2\n- should: 2\n- also: 1\n- be: 1\n- tested: 1\n- well: 1\n- work: 1\n\n'
		self.assertEqual(expected_output, output.decode('UTF8'))
