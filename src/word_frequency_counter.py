from collections import Counter

class WordFrequencyCounter:
	def __init__(self):
		self.words = []

	def load_from_string(self, words):
		self.words = words.split(' ')

	def load_from_file(self, filename):
		pass

	def summary(self):
		return dict(Counter(self.words))
