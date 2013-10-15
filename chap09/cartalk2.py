def counting(a,b,test_diff):
	diff=a-b
	if diff==test_diff:
		return 1
	else:
		return 0

def is_swaped(a,b,test_diff):
	af=a/10
	al=a%10
	bf=b/10
	bl=b%10
	count=0
	if af==bl and bf==al and a>b and counting(a,b,test_diff)>0:
		count+=counting(a,b,test_diff)
		print a,b
		return 1
	else:
		return 0
	
def run_tests(test_diff):
	count=0
	for a in range (100):
		for b in range(100):
			
			is_swaped(a,b,test_diff)
			count+=is_swaped(a,b,test_diff)
	print count,'count',test_diff,'age diff'


if __name__ == '__main__':
    test_diff=18
    for test_diff in range (10):
        run_tests((test_diff+1)*9)
#There is an 18 year age difference. The woman is 57. There is a strange behavior in this code that it prints the answers twice.
