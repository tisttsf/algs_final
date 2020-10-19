def gcd(a,b):#辗转相除
	if (b==0):return a
	r=a%b
	return gcd(b,r)
print (gcd(50,100))
x=[]

def gcd_normal(a,b):
	global x
	if (b%2==0 and a%2==0):x.append(2)
	gcd(a//2,b//2)
	return 2**(len(x)+1)
print (gcd_normal(36,100))



def gcd_more_advanced():
	pass
#辗转相减,最大公约数,最小公倍数,最大公约数
def function():
	pass