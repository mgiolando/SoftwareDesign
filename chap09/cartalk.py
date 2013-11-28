from palindrome import is_palindrome

def test(guess):
	"""Tests to see if the last 4 digits of guess,the last 5 digits of guess+1,and the digits of guess+2 are all palindromic.

	guess:int

	returns: int
	"""
	guess=str(guess).zfill(6)
	four=is_palindrome(guess[2:6])
	guess2=str(int(guess)+1).zfill(6)
	five=is_palindrome(guess2[1:6])
	guess3=str(int(guess)+2).zfill(6)
	six=is_palindrome(guess3[0:6])
	
	
	if four>0:
		if five>0:
			if six>0:
				print guess
				return guess



if __name__ == '__main__':
	for i in range (999999):
		test(000000+i)
		i+=1
#sample answers=098888 and 099999
