class WordFrequencyCounter:
	def load_from_string(self, words):
		self.words = words.split(' ')

	def count(self, word):
		return self.words.count(word)

	def summary(self):
		summary = {}
		for word in self.words:
			summary[word] = self.count(word)
		return summary

