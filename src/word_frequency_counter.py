from collections import Counter, OrderedDict
import operator

class WordFrequencyCounter:
	def __init__(self, words):
		self.words = words

	def summary(self):
		return dict(Counter(self.words))

	def textual_summary(self):
		summary_items = sorted(self.summary().items(), key=operator.itemgetter(0))
		summary_items = sorted(summary_items, key=operator.itemgetter(1), reverse=True)
		summary = ''
		for item in summary_items:
			summary += '- ' + item[0] + ': ' + str(item[1]) + '\n'
		return summary
