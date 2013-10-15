

def make_list():
	word_list=[]
	#fin=open('testwordlist.txt')
	fin=open('words.txt')
	for line in fin:
		entry=line.strip()
		word_list.append(entry)
	return word_list

def is_reverse_pair(a,b):
	return a[::-1] in b



if __name__ == '__main__':
    word_list=make_list()
    
    
    for word in word_list:
        if is_reverse_pair(word,word_list)==True:
            print word

