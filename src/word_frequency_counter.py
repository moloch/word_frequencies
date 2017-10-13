class WordFrequencyCounter:
	def load_from_string(self, words):
		self.words = words.split(' ')

	def count(self, word):
		return self.words.count(word)
