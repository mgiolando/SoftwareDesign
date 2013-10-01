import math

try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *

def koch(turtle, length, angle):
	if length<3:
		fd(turtle,length)
		return
	koch(turtle, length/3,angle)
	lt(turtle,angle)
	koch(turtle, length/3,angle)
	rt(turtle, 2*angle)
	koch(turtle, length/3,angle)
	lt(turtle, angle)
	koch(turtle, length/3,angle)
	

def snowflake(turtle, length,angle):
	for i in range (3):
		koch(turtle,length,angle)
		rt(turtle,120)



if __name__ == '__main__':
    world = TurtleWorld()    

    bob = Turtle()
    bob.delay = 0.001

    length=100
    angle=85
    koch(bob, length,angle)
#    snowflake(bob,length,angle)
    wait_for_user()
