def is_power(a,b):
    """Finds out if the number a is a power of b 
    a:int
    b:int

    returns: bool
    """
    if a%b==0:
	if a==b:
	    print True
	    return True
	else:
	    is_power(a/b,b)
    else:
	print False
	return False

def gcd(a,b):
    """Tests for the greatest common divisor between a and b.
    a:int
    b:int

    returns:int
    """
    r=a%b
    if r==0:
	print(b)
	return b
    gcd(b,r)
	

if __name__ == '__main__':
    is_power(16,2)
    gcd(72,45)
