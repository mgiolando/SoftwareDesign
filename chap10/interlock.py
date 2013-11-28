def interlock(word,word_list):
	"""Finds two words that interlcok to make a third word.
	
	word: string
	word_list: list

	returns: tuple #I didn't realize it was a tuple at the original time of writing
	"""
	word1=word[::2]
	word2=word[1::2]
	if word1 in word_list and word2 in word_list:
		print word,word1,word2
		return word1,word2
def interlock3(word,word_list):
	"""Finds three words that interlock to make a fourth word.
	
	word: string
	word_list: list

	returns: tuple #I didn't realize it was a tuple at the original time of writing
	"""
	word1=word[::3]
	word2=word[1::3]
	word3=word[2::3]
	if word1 in word_list and word2 in word_list and word3 in word_list:
		print word,word1,word2,word3
		return word1,word2,word3
	

if __name__ == '__main__':
    fin=open('words.txt')
    word_list=[]
    for line in fin:
	entry=line.strip()
	word_list.append(entry)
    for word in word_list:
	interlock(word,word_list)
        #interlock3(word,word_list)

