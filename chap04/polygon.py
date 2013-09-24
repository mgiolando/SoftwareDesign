#Mark Giolando
import math *
def square (t,length)	
	for i in range (4):
		bob=t
		fd(bob,length)
		lt(bob)

def polygon (t,length,n)
	for i in range (n):
		bob=t
		fd(bob,length)
		lt(bob,360/n)

def circle (t,r,length)
	n=2*math.pi*r/length
	for i in range (n):
		bob=t
		fd(bob,length)
		lt(bob,360/n)

def arc (t,r,length,angle)
	n=2*math.pi*r/length*angle/360

	for i in range (n):
		bob=t
		fd(bob,length)
		lt(bob,360/n)
