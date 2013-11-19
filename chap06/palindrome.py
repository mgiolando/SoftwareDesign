"""Module that provides is_palindrome.

Author of is_palindrome: you
"""

def first(word):
    """Returns the first character of a word.

    word: string

    returns: length 1 string
    """
    return word[0]


def last(word):
    """Returns the first character of a word.

    word: string

    returns: length 1 string
    """
    return word[-1]


def middle(word):
    """Returns all but the first and last character of a word.

    word: string

    returns: string
    """
    return word[1:-1]


def is_palindrome(word):
    """Returns if the input word is the same backwords as forwards. Word must be lowercase.

    word:string

    returns:bool"""
    # TODO: fill in the body of this function
    if first(word)==last(word):
    	if len(word)<=2:
    		print('yes it is')
    	else:
    		is_palindrome(middle(word))
    else:
	print('No it is not')
	return False

    return True

if __name__ == '__main__':
    is_palindrome('ppddpp')
