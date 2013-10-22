memo={}
memo['']=['']
def make_list():
	"""makes word list
	returns: list of strings"""
	fin=open('words.txt')
	word_list=[]
	for line in fin:
		entry=line.strip()
		word_list.append(entry)
	word_list.append('i')
	word_list.append('a')
	return word_list

def gen_children(a,word_list):
	child=[]
	for i in range(len(a)):
		test_child=a[:(i)]+a[(i+1):]
		if test_child in word_list:
			child.append(test_child)
		#	print test_child
	return child

def is_reducible(a,word_list):
	if a not in word_list:
		return False
	if a in memo:
		return memo[a]

#	child=[]
#	for i in range(len(a)):
#		test_child=a[:(i)]+a[(i+1):]
#		#print test_child
#		if test_child in word_list:
#			#print test_child
#			child.append(test_child)
#			is_reducible(test_child,word_list)
#removed previous lines of code ^ and placed in seperate function when things were running slow. Questionable effectiveness
	child =[]
	for word2 in gen_children(a,word_list):
		if is_reducible(word2,word_list) !=False:
			child.append(word2)
			
	memo[a]=child
	return child

def gen_reducible(word_list):
	outi=[]
	for word in word_list:
		word='sprite'
		k=is_reducible(word,word_list)
		outi.append(k)
	return outi

def is_longest(word_list):
	all_reducibles=gen_reducible(word_list)
	redlist=[]
	#print word_list
	for word in all_reducibles:
		redlist.append((len(word),word))
		
	redlist.sort(reverse=True)
	#print redlist[0]
	return redlist[0]

if __name__ == '__main__':
	word_list=make_list()
	print is_longest(word_list)

#something is broken that I can't find. Runs for very long time. Was working up to halfway through gen_reducible so about half of gen_reducible and is_longest is a best guess effort at what the answer might look like
