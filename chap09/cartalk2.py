def counting(a,b,test_diff):
	"""If a-b is equal to the test_diff, it returns a 1, if not it returns a 0.
	a: int
	b: int
	test_diff: int

	returns int
	"""
	diff=a-b
	if diff==test_diff:
		return 1
	else:
		return 0

def is_swaped(a,b,test_diff):
	"""Tests to see if a and b are reversed numbers.

	a:int
	b:int
	test_diff: int
	
	returns: int
	"""
	#a is the first number, in this case the mother's age
	#b is the second number tested, in this case the daughter's age
	af=a/10 #af is the first number of a
	al=a%10 #al is the last number of a
	bf=b/10 #bf is the first number of b
	bl=b%10 #bl is the first number of b
	count=0
	if af==bl and bf==al and a>b and counting(a,b,test_diff)>0:
		count+=counting(a,b,test_diff)
		if abs(a-b)==18 and a>b:#I found the age difference was 18. Then I came back to add this to print out the times the ages were reversed adn counted to reach the answer.
			print a,b
		return 1
	else:
		return 0
	
def run_tests(test_diff):
	"""Runs the tests which compare the given test_diff to numbers between 1 and 100.

	test_diff: int
	"""
	count=0
	for age_moth in range (100):
		for age_daug in range(100):
			
			is_swaped(age_moth,age_daug,test_diff)
			count+=is_swaped(age_moth,age_daug,test_diff)
	if count ==8:
		print test_diff,'age diff'

if __name__ == '__main__':
    for test_diff in range (10):
        run_tests((test_diff+1)*9)
#There is an 18 year age difference. The woman is 57.
