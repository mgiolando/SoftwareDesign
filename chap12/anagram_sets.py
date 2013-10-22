import itertools

def word_perm(a):
	"""generates all permutations of the given word in a list

	a:string
	Returns: list of strings"""
	a=list(a)	
	perm_list=list(itertools.permutations(a))
	for i in range (len(perm_list)):
		perm_list[i]=''.join(perm_list[i])
	return perm_list
def make_small_list(word_list):
	"""creates a list of 8 letter words
	word_list: list of strings
	returns: a list of strings"""
	eightletters=[]
	for word in word_list:
		if len(word)==8:
			eightletters.append(word)
	return eightletters
def anagrams_sort(tobe):
	""" sorts a list in reverse order
	tobe: list of strings
	returns: a list of strings"""
	outgoing=sorted(tobe,reverse=True)
	return outgoing
def anagrams(a,word_list):
	"""takes a list of strings and sorts out which are actually words. Then has them sorted by angrams_sort
	a: list of strings
	word_list: list of strings
	returns: list of strings"""
	res=[]
	for i in range(len(a)):
		if a[i] in word_list:
			res.append(a[i])
	res=anagrams_sort(res)
	return res
def count_bingo(a,word_list):
	"""Finds out which words in the input list have the most anagrams
	a:list of strings
	word_list: list of strings
	returns: list of strings"""
	d=dict()
	t=[]
	for word in a:
		d[word]=len(anagrams(word_perm(word),word_list))
		t.append((len(anagrams(word_perm(word),word_list)),word))
	t.sort(reverse=True)
	old_number=0
	collect=[]
	for i in range(len(t)):
		number, words=t[i]
		if number>=old_number:
			collect.append(words)
			#print words
			old_number=number		
	return collect
	

if __name__ == '__main__':
	fin=open('words.txt')
	word_list=[]
	for line in fin:
		entry=line.strip()
		word_list.append(entry)
	eightletters=make_small_list(word_list)
	for word in word_list:
		anagrams(word_perm(word), word_list)
	#This finds all anagrams and sorts their components in decresing order

	print count_bingo(test,word_list)
	#this finds the best bingo words, takes a while

