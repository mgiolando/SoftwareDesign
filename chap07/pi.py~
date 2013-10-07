import math
def factorial(n):
	if n==0:
		return 1
	else:
		recurse=factorial(n-1)
		result=n*recurse
		return result
def sum_calculation(k,c2):
	e=10**-15
	part1=2*math.sqrt(2)/9801
	part2=(factorial(4*k))*(1103+26390*k)
	part3=factorial(k)**4
	part4=396**(4*k)
	c=part2/(part3*part4)
	
	while c>e:
		k=k+1
		c=c+c2
		sum_calculation(k,c)
		return c
	print c2
	answer=1/(part1*c2)
	print answer
	return answer

def estimate_pi(k):
	part1=2*math.sqrt(2)/9801	
	sumcalc=sum_calculation(k,0)
	

if __name__ == '__main__':
    
    estimate_pi(0.0)
    
