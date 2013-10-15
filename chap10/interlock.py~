

def interlock(a,b):
	t=[]
	if len (a)>=len(b):
		for i in range (len (a)):
			t.append(a[i])
			t.append(b[i])
	if len (b)>len(a):	
		for i in range (len (a)):
			t.append(a[i])
			t.append(b[i])
	t=''.join(t)
	if t in word_list:
		print t, a, b
	return t
def will_work(a,b):
	if len(a)==len(b):
		interlock(a,b)


if __name__ == '__main__':
    fin=open('words.txt')
    #fin=open('testwordlist.txt')
    word_list=[]
    for line in fin:
	entry=line.strip()
	word_list.append(entry)
    for i in range(len(word_list)):
	for j in range(len(word_list)):
	    will_work(word_list[i],word_list[j])
    will_work('shoe','cold')

#Very slow to run, recommend using testwordlist.txt instead of words.txt as it is a much shorter list. For words.txt the first answer is avails from aal and vis and takes 4 minutes to reach
#even=[::2]
#odd=[1::2]


   
