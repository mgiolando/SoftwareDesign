def is_power(a,b):
	if a%b==0:
		if a==b:
			return(True)
		else:
			is_power(a/b,b)
	else:
		return(False)

def gcd(a,b):
	
	r=a%b
	if r==0:
		print(b)
		return
	gcd(b,r)
	

if __name__ == '__main__':
#    is_power(16,2)
    gcd(60,18)
