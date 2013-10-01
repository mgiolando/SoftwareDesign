import math

try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *

def turnright(turtle,angle,length):
	#angle=90
	rt(turtle,angle)
	fd(turtle,length)

def turnleft(turtle,angle,length):
	#angle=90
	lt(turtle,angle)
	fd(turtle,length)

def runningdragon(turtle, length, angle, count):
	count=count-1
	if count>0:
		turnright(turtle,angle,length)
		runningdragon(turtle,length,angle,count)
		turnleft(turtle,2*angle,length)
		runningdragon(turtle,length,-angle,count)
		turnright(turtle,angle,length)
	else:
		fd(turtle,length)




if __name__ == '__main__':
    world = TurtleWorld()    

    bob = Turtle()
    bob.delay = 0.001

    length=1
    angle=45
    count=8
    runningdragon(bob, length, angle, count)

    wait_for_user()
