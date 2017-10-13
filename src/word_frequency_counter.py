class WordFrequencyCounter:
	def load_from_string(self, words):
		self.words = words

	def count(self, word):
		if word in self.words.split():
			return 1
		else:
			return 0
