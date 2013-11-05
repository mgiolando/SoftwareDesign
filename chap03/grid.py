#Mark Giolando
def top_row():
	print '+','-','-','-','-','+','-','-','-','-','+'
def mid_row():
	print '|',' ',' ',' ',' ','|',' ',' ',' ',' ','|'


def top_row2():
	print '+','-','-','-','-','+','-','-','-','-','+','-','-','-','-','+','-','-','-','-','+'
def mid_row2():
	print '|',' ',' ',' ',' ','|',' ',' ',' ',' ','|',' ',' ',' ',' ','|',' ',' ',' ',' ','|'


if __name__ == '__main__':
	top_row()
	for i in range(2):
		for j in range(4):
			mid_row()
		top_row()

	top_row2()
	for i in range(4):
		for j in range(4):
			mid_row2()
		top_row2()

