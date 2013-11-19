import math
def factorial(n):
	"""Calculates the facotrial of the input number.
	n:int
	
	returns:int
	"""
	if n==0:
		return 1
	else:
		recurse=factorial(n-1)
		result=n*recurse
		return result
def estimate_pi(k,carry_over):
	"""Estimates the value for pi given an estimate.
	k: int
	carry_over:float
	
	returns float
	"""
	e=10**-15
	part1=2*math.sqrt(2)/9801
	part2=(factorial(4*k))*(1103+26390*k)
	part3=factorial(k)**4
	part4=396**(4*k)
	kth_term=part2/(part3*part4)
	
	while kth_term>e:
		k=k+1
		kth_term=kth_term+carry_over
		estimate_pi(k,kth_term)
		return kth_term
	answer=1/(part1*carry_over)
	print answer
	return answer

if __name__ == '__main__':
	estimate_pi(0,0.0)
