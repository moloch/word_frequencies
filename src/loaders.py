import re

class StringLoader:

	def load(self, words_string):
		words_string = re.sub('[!.,?]', '', words_string)
		return words_string.lower().split()

class FileLoader:

	def load(self, filename):
		with open(filename, 'r') as file:
			words_string = ''
			for line in file:
				line = re.sub('[!.,?]', '', line)
				words_string += " " + line
			return words_string.lower().split()