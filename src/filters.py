class FileFilter:

	def __init__(self, filename):
		self.filename = filename

	def filter(self, word_list):
		with open(self.filename, 'r') as file:
			banned_words = []
			for line in file:
				banned_words.extend(line.lower().split())
			return [x for x in word_list if x not in banned_words]