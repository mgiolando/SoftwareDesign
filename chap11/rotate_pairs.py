from rotate import rotate

def rotate_pair(word2be,word_list):
	"""This run the program to find the rotated words for the given word.
	word2be: string
	word_list: list of strings"""
	for i in range(13):
		test_word=rotate(word2be,i+1)
		if test_word in word_list:
			print word2be, test_word
			

if __name__ == '__main__':
	fin=open('words.txt')
	word_list=[]
	for line in fin:
		entry=line.strip()
		word_list.append(entry)

	for word in word_list:
		rotate_pair(word,word_list)




