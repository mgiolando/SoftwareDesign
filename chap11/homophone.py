from pronounce import read_dictionary

def is_homophone(word_a,word_b,saying):
	""" This function checks to see if two words are both homophones and in the list saying
	word_a: string
	word_b:string
	saying: dictionary
	returns: bool"""
	#is in pronounce?
	if word_a not in saying or word_b not in saying:
		return False
	#is same pronounciation
	word_asaying=saying[word_a]
	word_bsaying=saying[word_b]
	return word_asaying==word_bsaying

def is_crit(word_a,saying):
	"""This checks to see if the word that is guessed matches the criteria of the problem. That is to say if it is 5 letters long, has only 1 syllable and is in the dictionary.
	word_a: string
	saying: dictionary
	returns: bool"""
	if word_a not in saying:
		return False
	pro=saying[word_a]
	t= pro.split( )
	count=0
	if len(word_a)!=5:
		return False
	count=0
	for i in range(len(t)):
		if len(t[i])>2:
			count+=1
	if count!=1:
		return False
	else: 
		return True

def run_test(word1,saying):
	"""This runs the tests and the function as a whole.
	word1: string
	saying: dictionary"""
	word2=word1[1:]
	word3=word1[0]+word1[2:]
	if is_crit(word1,saying) and is_homophone(word1,word2,saying) and is_homophone(word1,word3,saying)==True:
		print word1,word2,word3

if __name__ == '__main__':
	fin=open('words.txt')
	word_list=[]
	for line in fin:
		entry=line.strip()
		word_list.append(entry)
	saying=read_dictionary()
	for word in word_list:	
		if len(word)==5:
			run_test(word,saying)

