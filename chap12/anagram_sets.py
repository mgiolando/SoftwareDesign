def letters(word):
	"""This section sorts a string by the letters that make it up and returns them as a string.
	word: string
	returns: string
	"""
	l=list(word)
	l.sort()
	l=''.join(l)
	return l

def anagram_dict():
	"""Creates a dictionary of all anagrams by the letters that make them up

	returns: dict
	"""
	d={}
	fin=open('words.txt')
	for line in fin:
		entry=line.strip().lower()
		l=letters(entry)
		if l not in d:
			d[l]=[entry]
		else:
			d[l].append(entry)
	return d
def print_anagram_dict():
	"""Prints all anagrams as created by a dictionary.
	"""

	for vals in d.values():
		print vals


def largest_anagram(d):
	""" Sorts a dictionary by the size of the length of their key
	d: dict
	returns: list
	"""
	t=[]
	for vals in d.values():
		t.append((len(vals),vals))
	t.sort(reverse=True)
	return t

def bingo(d):
	"""Returns the set of letters that allow for the most bingo wins.
	d: dict
	returns: string
	"""
	res=[]
	for key, value in d.iteritems():
		if len(key)==8:
			res.append((len(value),key))
	res.sort(reverse=True)
	num,letters =res[0]
	return letters
if __name__ == '__main__':
	d=anagram_dict()
	print_anagram_dict()
	print largest_anagram(d)
	print bingo(d)

