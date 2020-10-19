c=[4,5,6,7,8,6,5,4,3,2,1]

def peak_1():
	for i in range(len(c)):
		if i==0:
			if c[i+1]<c[i]:
				return i
		elif i==len(c)-1:
			if c[i-1]<c[i]:
				return i
		else:
			if c[i+1]<c[i] and c[i-1]<c[i]:
				return i
d=peak_1()
print (d)
c=[4,5,6,7,8,9,10,11,12,2,1]
def peak_2(start,end):
	mid=(start+end)//2
	if mid==0:
		if c[mid]>c[mid+1]:
			return mid
		else:
			return None
	if mid==len(c)-1:
		if c[mid]>c[mid-1]:
			return mid
		else:
			return None
	if c[mid]<c[mid-1]:
		return peak_2(start,mid-1)
	elif c[mid]<c[mid+1]:
		return peak_2(mid+1,end)
	else:
		return mid,c[mid]

print (peak_2(0,len(c)-1))





	
"找任意三个片段峰值的算法"