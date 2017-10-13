from collections import Counter, OrderedDict

class WordFrequencyCounter:
	def __init__(self):
		self.words = []

	def load_from_string(self, words_string):
		self.words = words_string.lower().split()

	def load_from_file(self, filename):
		with open(filename, 'r') as file:
			data = ''
			for line in file:
				data += " " + line.strip().replace('.', '')
			self.load_from_string(data)

	def summary(self):
		return dict(Counter(self.words))

	def textual_summary(self):
		summary_items = sorted(self.summary().items(), key=lambda t: t[1], reverse=True)
		summary = ''
		for item in summary_items:
			summary += '- ' + item[0] + ': ' + str(item[1]) + '\n'
		return summary
