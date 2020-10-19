from itertools import zip_longest
import sys,io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')



for d,p in zip_longest({1:0,2:0,3:0,4:0},{2:0,3:0,4:0}):
	print (d,p)
from random import randint

a=list(range(10))
with open("text.txt","w+") as f:
	f.writelines(["1","2","3"])

print ("用时 {}".format(1))
print ("用时 %d"%100)

print (5**11)
t=[0,1]
for i in range(2,40):
	nt=t[i-1]+t[i-2]
	t.append(nt)
print ()
print (randint(3,4))
print (randint(2,4))
print (randint(2,4))
