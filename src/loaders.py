class StringLoader:

	def load(self, words_string):
		return words_string.lower().replace('.','').split()

class FileLoader:

	def load(self, filename):
		with open(filename, 'r') as file:
			words_string = ''
			for line in file:
				words_string += " " + line.strip().replace('.', '')
			return words_string.lower().split()