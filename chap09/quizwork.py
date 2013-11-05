def list_intersection(a,b):
	both_list=[]
	both_list2=[]
	if len(a)>len(b):
		for k in range(len(a)-1):
			if a[k] in b:
				both_list.append(a[k])
				#print a[k]
	if len(b)>len(a):
		for k in range(len(b)-1):
			if a[k] in b:
				both_list.append(a[k])
				#print a[k]
	print both_list


c=[3,2,1]
d=[1,3,5,7]
list_intersection(c,d)
