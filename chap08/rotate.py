def rotate(a,b):
	length=len(a)
	k=0
	while k < length:
		m=chr(ord(a[k])+7)
		print m,
		k=k+1


#	print ord('c')
#	print chr(ord('c'))



if __name__ == '__main__':
	a='cheer'
	b=7
	rotate(a,b)
