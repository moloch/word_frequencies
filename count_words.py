import sys
from src.word_frequency_counter import WordFrequencyCounter
from src.loaders import FileLoader

def count_words():
	wfc = WordFrequencyCounter(FileLoader().load(sys.argv[1]))
	header = 'Word frequencies for ' + sys.argv[1] + ':\n'
	print(header + wfc.textual_summary())

if __name__ == '__main__':
	count_words()
