"12/02"
from algs_rc_nchoosek import permutation_nonrepeated
p=permutation_nonrepeated(["x","y","z"],3,[],[])
print (p)
def a(x,y,z):
	print ("%s->%s %s->%s %s->%s"%(x,z,x,y,z,y))
def b(x,y):
	print ("%s->%s"%(x,y))

def ta_logic(n,x,y,z,a,b):
	if n==0:
		return
	if n==1:
		b(x,z)
		ta(t-1,"y","x","z",a,b,t=t-1)
	a(x,y,z)
	if x=="x" and y=="y" and z=="z":	
		b("x","z")
		f(a,"y","x","z")
	elif x=="y" and y=="x":
		pass
	# 	b("z","y")
	# 	f(,"x","y","z")
	# elif x=="y" and y=="z":
	# 	b("x","z")
	# 	f(,"","","")
	# elif x=="z" and y=="y" and z=="z":
	# 	b(                           )
	# 	f(,"","","")
	# elif x==""
	# elif x=="z" and z=="x":
	# 	b(y,z)
	# 	f("x","y","z")
from random import randint
which_ta=randint(1,2)
a,b,c=[],[],[1,2,3,4,5,6,7,8]
def programming():
	this_ta=randint(1,2)
	c=[]
	temp_len=len(c)
	while len(c)>=0:
		try:
			temp_el1=c.pop(0)#这里也换了
			temp_el2=c.pop(0)#这里也换了
			temp_el3=c.pop(0)#这里也换了#同时因为还要考虑是不是被3整除的问题
		except:
			print ("sucess,end,heat-chromsom")
		this_ta=1
		if this_ta==1:#
			# a=[]
			while len(a)!=temp_len:#and
				a.insert(0,temp_el1)#append()
				# b=[]
				b.insert(0,temp_el2)#append()
				xx=a.pop(0)
				b.insert(0,xx)
				a.append(temp_el3)
				# b,c,a=c[:],a[:],b[:]
				break
				# print (b,c,a)
		break
				#这种方法并不能到底部
				#在第一盘到底部之后,还要重新转换一次
		# elif this_ta==2: 
		# 	while len(b)!=temp_len:#and
		# 		b.insert(0,temp_el1)#append()
		# 		a.insert(0,temp_el2)#append()
		# 		xx=b.pop(0)
		# 		a.insert(0,xx)
		# 		b.append(temp_el3)
		# 		a,c,b=c[:],b[:],a[:]
		# 		在第一盘到底部之后,还要重新变换一次

"换柱子需要(同样但是稍有不同)转换器"

programming()
print (a,b,c)



#这里有一个新问题 将acb 填满四个空间 有多少种可能
