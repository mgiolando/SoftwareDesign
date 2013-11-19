from swampy.TurtleWorld import *

def turnright(turtle,angle,length):
	"""This function turns the turtle right.
	turtle: object
	angle: int
	length: int
	"""
	rt(turtle,angle)
	fd(turtle,length)

def turnleft(turtle,angle,length):
	"""This function turns the turtle left.
	turtle: object
	angle: int
	length: int
	"""
	lt(turtle,angle)
	fd(turtle,length)

def runningdragon(turtle, length, angle, count):
	"""This function draws a dragon curve.
	turtle: object
	angle: int
	length: int
	count: int
	"""
	count-=1
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
