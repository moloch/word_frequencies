from collections import Counter

class WordFrequencyCounter:
	def load_from_string(self, words):
		self.words = words.split(' ')

	def summary(self):
		return dict(Counter(self.words))
