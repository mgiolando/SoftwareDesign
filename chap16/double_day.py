import datetime
from datetime import date

def day_of_the_week():
	"""This function prints the day of the week for the current day.
	Returns: string
	"""
	weekdays=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
	today=datetime.date.today()
	print weekdays[datetime.date.weekday(today)]

def birthday_age(birth):
	"""This function calculates someone's age and how long until their next birthday. If the person has not been born yet, this program says so.
	
	birth=tuple

	Returns: int, datetime.timedelta, string
	"""
	today=datetime.date.today()
	birthday=datetime.date(birth[0],birth[1],birth[2])
	birthday2=birthday.replace(year=today.year)
	print 'They are',
	

	if birthday2>today:
		print "not yet born"
		#print today.year-birthday.year-1
	elif birthday2==today:
		print "newly born"
	else:
		print "lesser"
		print today.year-birthday.year
	today=datetime.datetime.today()
	today=today.replace(microsecond=0)
	birthday3=datetime.datetime(today.year,birth[1],birth[2])
	if birthday3<today:
		birthday.replace(year=today.year+1)
	days_to_birthday=abs(today-birthday3)
	print 'Their  birthday will be in:',
	if birthday3<=today:
		print days_to_birthday
	
def double_day(a,b,n=2):
	"""This function calculates when one person will be n times the age as the other with 2 being the default.
	a: tuple
	b: tuple
	
	returns: datetime.date, string
	"""
	a=datetime.date(a[0],a[1],a[2])
	b=datetime.date(b[0],b[1],b[2])
	older_age=abs(a-b)*n	#in days
	print 'One person will be %d times the other on'%n,
	if a>b:
		print a+older_age
	elif b>a:
		print b+older_age
	elif b==a:
		print 'Never, they are the same age'
if __name__ == '__main__':
	day_of_the_week()
	birthday_age((2013,12,17))
	double_day((1982,11,10),(1992,11,10),2)


