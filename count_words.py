#!/usr/bin/env python
import sys
from src.word_frequency_counter import WordFrequencyCounter
from src.loaders import FileLoader
from src.filters import FileFilter

def count_words():
	words_list = FileLoader().load(sys.argv[1])
	if len(sys.argv) == 3:
		words_list = FileFilter(sys.argv[2]).filter(words_list)
	wfc = WordFrequencyCounter(words_list)
	header = 'Word frequencies for ' + sys.argv[1] + ':\n'
	print(header + wfc.textual_summary())

if __name__ == '__main__':
	count_words()
