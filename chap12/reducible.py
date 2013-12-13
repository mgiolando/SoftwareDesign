memo={}
memo['']=['']
def make_list():
	"""makes word dictionary
	returns: dict of strings"""
	fin=open('words.txt')
	word_list={}
	for line in fin:
		entry=line.strip().lower()
		word_list[entry]=entry
	word_list['a']='a'
	word_list['i']='i'
	word_list['']=''
	return word_list

def gen_children(word,word_list):
	"""generates a list of child words from a given word
	word: string
	word_list: dict
	"""
	child=[]
	for i in range(len(word)):
		test_child=word[:(i)]+word[(i+1):]
		if test_child in word_list:
			child.append(test_child)
	return child

def is_reducible(word,word_list):
	"""tests a word to see if it is reducible
	word: string
	word_list: dict
	returns: bool or list
	"""
	if word not in word_list:
		return False
	if word in memo:
		return memo[word]

	res =[]
	for word2 in gen_children(word,word_list):
		if is_reducible(word2,word_list):
			res.append(word2)
			
	memo[word]=res
	return res

def total_reducible(word_list):
	"""creates a list of all reducible words
	word_list:dict
	returns: list
	"""
	res=[]
	for word in word_list:
		temp=is_reducible(word,word_list)
		if temp != []:
			res.append(word)
	return res
def longest_reducible(red_list):
	""" finds the longest reducible word by sorting red_list by size
	red_list: list
	returns: list
	"""
	res=[]
	for word in red_list:
		res.append((len(word),word))
	res.sort(reverse=True)
	length_of,longest_word=res[0]
	print longest_word, length_of
	return res

if __name__ == '__main__':
	word_list=make_list()
	red_list=total_reducible(word_list)
	longest_reducible(red_list)
