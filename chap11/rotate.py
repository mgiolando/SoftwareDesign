def rotate(word_to_rotate,how_much):
	"""Rotates the letters of word_to_rotate by how_much.
	word_to_rotate: string
	how_much: int
	
	returns: string
	"""
	how_much-=26*(how_much/26)	
	
	length=len(word_to_rotate)
	k=0
	word=[0]*len(word_to_rotate)
	while k < length:
		m_ord=ord(word_to_rotate[k])+how_much
		if m_ord>122:
			m_ord-=26

		m_chr=chr(m_ord)
		word[k]=m_chr		
		#print m,
		k=k+1
	word2=''.join(word)
	return word2




if __name__ == '__main__':
	word_to_rotate='zcheer'
	how_much=59
	print rotate(word_to_rotate,how_much)
