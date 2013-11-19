def rotate(word,b):
	"""Rotates the letters of a word by b.
	word: string
	b: int
	
	returns: string
	"""
	length=len(word)
	count=0
	holder2=''
	while count < length:
		holder=chr(ord(word[count])+7)
		holder2=holder2+holder
	
		count+=1
	print holder2
	return holder2

if __name__ == '__main__':
	a='cheer'
	b=7
	rotate(a,b)
