import urllib
#conn = urllib.urlopen('http://thinkpython.com/secret.html')
#for line in conn:
#	print line.strip()
#'http://www.uszip.com/zip/02492'

if __name__ == '__main__':
    var=raw_input("Enter a Zipcode: ")
    address='http://www.uszip.com/zip/'+var
    conn=urllib.urlopen(address)
    t=[]
    for line in conn.fp:
	line=line.strip()
	if '<title>' in line:
	    line.split()
	    print line[7:-16]
	if 'Total population' in line:
	    line=line.strip('z')
	    loc=line.index('Total population')
	    loc2=line.index('<span')
	    print line[(loc+25):loc2]
	    
