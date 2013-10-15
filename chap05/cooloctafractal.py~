import math

try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *


def turnright(turtle,length,angle):
	rt(turtle,angle)
	fd(turtle,length)
def turnleft(turtle,length,angle):
	lt(turtle,angle)
	fd(turtle,length)
def turnabright(turtle,length):
#will turn right no matter the angle
	rt(turtle,90)
	fd(turtle,length)
def rundragon(turtle,length,angle,count):
	count=count-1
	if count>0:
		turnright(turtle,length,angle)
		rundragon(turtle,length,angle,count)
		turnleft(turtle,length,angle)
		rundragon(turtle,length,angle,count)

if __name__ == '__main__':
    world = TurtleWorld()    

    bob = Turtle()
    bob.delay = 0.001

    length=1
    angle =90
    count=16
    rundragon(bob,length,angle,count)
    wait_for_user()
