TAX_RATE=0.1
import decimal


def betrate_last(a,b):#
	return round(a/b,2),round(b/a,2)

def betrate_predict(pre_a,pre_b,a,b,amount):#a,b的两次通过amount下注后产生的赔率差
	d1,d2=abs(a-pre_a),abs(pre_b-b)
	true_b=amount/d1
	tmp=true_b*amount/d2
	true_a=sqrt(tmp+(amount/2)**2)-amount/2
	return true_a,true_b




#for i in range(1,1000):
#	for j in range(1,1000):
#		a,b=betrate_last(i,j)
#		if a==0.44:
#			print (b)

from math import sqrt
print (sqrt(27225)-15)

record="""
82,0
10,0
12,0
31,0
20,33.4
10,0
35,61.25
17,35.19
10,20.5
50,0
35,0
106,166.42
10,14.9
30,53.7
15,27
139,0
33,0
10,20.6
10,0
10,0
10,0
23,0
30,63.0
14,21.7
256,739.84
688,0
100,183
600,0
46,0
280,0
150,0
40,82
88,0
100,0
45,0
300,735
45,109.8
66,0
16,0
20,0
35,54.25
88,205.04
150,271.5
100,198
50,150
30,57.9
60,0
38,0
35,0
66,137.28
66,157.08
20,26
36,104.04
150,0
50,0
12,24.24
100,212
38,0
33,0
233,0
100,0
35,0
230,476.1
130,257.4
36,64.44
188,503.84
100,224.00
200,0
266,0
260,0
30,0
50,0
10,0
30,0
30,0
39,54.21
175,406
30,0
25,0
50,0
10,0
10,0
20,38.8
50,92.00
50,95
50,90.5
10,0
12,0
88,0
10,0
"""
c=record.split("\n")
s,se=0,0
for i in c[1:-1]:
	t=i.split(",")
	a,b=float(t[0]),float(t[1])
	s+=a
	if b!=0:
		se+=(b-a)
print (s,se)




