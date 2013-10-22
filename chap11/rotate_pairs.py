def rotate(a,b):
	"""This roates the word a by an integer b.
	a: string
	b: integer
	returns: string
"""
	length=len(a)
	k=0
	word=[0]*len(a)
	while k < length:
		init=ord('a')	#initial letter starting point
		letterr=ord(a[k])-init	#mispelling to be on safe side
		m=chr((letterr+b)%26+init)
		word[k]=m		
		k=k+1
	word2=''.join(word)
	return word2

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




