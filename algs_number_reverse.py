

def printout(n):
	if n%10==n:
		print (n)
	else:
		print (n%10,end="")
		printout(n//10)

printout (23541)

# def printc(n):
# 	if n//(10**4)==0:
# 		print (n)
c=[1,2,3,4,4,4,4,5,5,5]
d=[4,5]
