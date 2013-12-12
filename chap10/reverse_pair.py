def make_list():
	"""Creates a list of strings from a saved file.
	"""
	word_list=[]
	fin=open('words.txt')
	for line in fin:
		entry=line.strip()
		word_list.append(entry)
	return word_list

def is_reverse_pair(word,word_list):
	"""Checks if reversed word is in wordlist.
	
	word: string
	word_list: list

	returns: bool
	"""
	return word[::-1] in word_list



if __name__ == '__main__':
	word_list=make_list()

	for word in word_list:
	        if is_reverse_pair(word,word_list)==True:
			print word, word[::-1]

