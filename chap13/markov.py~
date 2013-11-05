"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

import string
import random

prefix=()
suffixes={}

def process_file(filename, skip_header=True, order=2):
    """Makes a histogram that contains the words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
   
    Returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = file(filename)

    if skip_header:
        skip_gutenberg_header(fp)
#Wasn't able to make progress at first, had to look this up between the comments.
    for line in fp:
	for word in line.rstrip().split():	
	        process_word(word, order)
#Just this part. 		
    return hist


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*END*THE SMALL PRINT!'):
            break
def process_word(word,order=2):
	"""Creates a dictionary containing words that follow a pair.

	word:string
	order:int"""
    global prefix
    if len(prefix)<order:
	prefix+=(word,)
	return
    try:
	suffixes[prefix].append(word)
    except KeyError:
	suffixes[prefix]=[word]
    prefix=new_prefix(prefix,word)

def new_prefix(prefix,word):
	"""updates the prefix by changing out the zeroth element and adding another word
	prefix:tuple
	word:string
	returns:tuple"""
    return prefix[1:]+ (word,)

def cont_word(reps=20,order=2):
	"""creates a string of words length reps of markov words
	reps:int
	order:int
	returns:string"""
    first=random.choice(suffixes.keys())
    for j in range(order):
         print first[j],

    for i in range(reps):
	cont=suffixes.get(first,None)
	next_word=random.choice(cont)
	print next_word,
	first=first[1:]+(next_word,)
#There are some problems where it repeats similar words.	

if __name__ == '__main__':
    hist = process_file('emma.txt', skip_header=True)
    words = process_file('words.txt', skip_header=False)
    cont_word()

