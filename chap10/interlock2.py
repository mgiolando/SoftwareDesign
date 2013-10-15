

def interlock(k,word_list):
	word1=k[::2]
	word2=k[1::2]
	if word1 in word_list and word2 in word_list:
		print k,word1,word2
		return word1,word2
def interlock3(k,word_list):
	word1=k[::3]
	word2=k[1::3]
	word3=k[2::3]
	if word1 in word_list and word2 in word_list and word3 in word_list:
		print k,word1,word2,word3
		return word1,word2,word3
	

if __name__ == '__main__':
    fin=open('words.txt')
    word_list=[]
    for line in fin:
	entry=line.strip()
	word_list.append(entry)
    for i in range(len(word_list)):
	#interlock(word_list[i],word_list)
        interlock3(word_list[i],word_list)

