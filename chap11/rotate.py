def rotate(a,b):
	length=len(a)
	k=0
	word=[0]*len(a)
	while k < length:
		m=chr(ord(a[k])+7)
		word[k]=m		
		#print m,
		k=k+1
	word2=''.join(word)
	return word2




if __name__ == '__main__':
	a='cheer'
	b=7
	print rotate(a,b)
