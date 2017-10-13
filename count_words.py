import sys
from src.word_frequency_counter import WordFrequencyCounter

if __name__ == '__main__':
	wfc = WordFrequencyCounter()
	wfc.load_from_file(sys.argv[1])
	print(wfc.summary())