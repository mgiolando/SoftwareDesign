from swampy.TurtleWorld import *
def koch(turtle, length, angle):
	"""Draws a Koch curve fractal.
	turtle: object
	length: int
	angle: int
	"""
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
	"""This function draws a snowflake. This is done by making a triangle in which each side is a koch curve
	turtle: object
	length: int
	angle: int
	"""
	for i in range (3):
		koch(turtle,length,angle)
		rt(turtle,120)



if __name__ == '__main__':
	world = TurtleWorld()    

	bob = Turtle()
	bob.delay = 0.001

	length=100
	angle=85
	#only koch or snowflake can be run at a time
	koch(bob, length,angle)
	#snowflake(bob,length,angle)
	wait_for_user()
