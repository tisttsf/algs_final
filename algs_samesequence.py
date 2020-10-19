a=[1,2,3,3,4]
#1
#2
def x_1(a,b):
	for i in a:
		if i not in b:
			b.append(i)
	for i in b:
		if i not in a:
			a.append(i)
	return a,b,set(a)==set(b)


def x_2(a,b):
	for i in a:
		for j in range(abs(a.count(i)-b.count(i))):
			b.append(i)
	for i in b:
		for j in range(abs(a.count(i)-b.count(i))):
			a.append(i)
	return a,b,set(a)==set(b)

a,b=[1,2,4],[4,5,7,10,11]
print (x_1(a,b))
print (x_2(a,b))