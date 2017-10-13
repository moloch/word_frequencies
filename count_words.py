import sys
from src.word_frequency_counter import WordFrequencyCounter

def count_words():
	wfc = WordFrequencyCounter()
	wfc.load_from_file(sys.argv[1])
	header = 'Word frequencies for ' + sys.argv[1] + ':\n'
	print(header + wfc.textual_summary())

if __name__ == '__main__':
	count_words()
