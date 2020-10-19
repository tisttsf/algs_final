def x_2(a,b):
	atob=[]
	for i in a:
		if i not in b:
			for j in range(abs(a.count(i)-b.count(i))):
				atob.append(i)
	delete=[]
	for i in b:
		if i not in a:
			for j in range(abs(a.count(i)-b.count(i))):
				delete.append(i)
	return atob,delete

class Ab(object):
	def __init__(self):
		pass
	