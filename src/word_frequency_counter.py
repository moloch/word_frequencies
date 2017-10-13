from collections import Counter

class WordFrequencyCounter:
	def __init__(self):
		self.words = []

	def load_from_string(self, words):
		self.words = words.split(' ')

	def load_from_file(self, filename):
		with open(filename, 'r') as file:
			data = ''
			for line in file:
				data += " " + line.strip().replace('.', '')
			self.load_from_string(data)

	def summary(self):
		return dict(Counter(self.words))
