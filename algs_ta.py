def f(n,a,b,c):
    if n==1:
        print ("%s->%s",c,b)
    if n==2 and c=="3" and b=="2":
        print ("%s->%s %s->%s"%(c,b,c,a))
    if c=="3" and b=="2":
        print ("%s->%s %s->%s %s->%s %s->%s"%(c,a,c,b,a,b,c,a)) 
        f(n-1,c,a,b)
    if a=="3" and b=="1":
        print (	"%s->%s %s->%s %s->%s %s->%s"%(b,a,b,c,a,c,a,b)) 
        f(n-1,b,c,a)
    f(n,a,b,c)


    # print ("%s->%s %s->%s %s->%s"%(c,a,c,b,a,b))
# f(4,"1","2","3")

# def income(n,a=3000,b=1000,c=300,d=50):
#     if n==0:
#         return (5000*1+1500*3+500*7+76*24)
#     return (a+b*3+c*7+d*24)+income(n-1)
# print (income(1)*5/12)
from algs_rc_nchoosek import permutation_nonrepeated
p=permutation_nonrepeated(["x","y","z"],3,[],[])


def a(x,y,z):
	print ("%s->%s %s->%s %s->%s"%(x,y,x,z,y,z))
def b(x,y):
	print ("%s->%s",x,y)

def ta_listversion(x,y,z,a,b,c):
	

def ta(x,y,z,a,b,c):
	if n==0:
		return
	if n==1:
		b(x,z)
		ta(t-1,"y","x","z",t=t-1)
	else:
		b(x,da)

# 	else:
# 		a(x,y,z)
# 		if x=="x" and z=="z":
# 			b(x,y)
# 			ta(n,"z","y","x")
# 		elif x=="z" and z=="x":
# 			b(y,z)
# 			ta(n,"x","y","z")


	# def hano(n,x,y,z):
# 	if n==1:
# 		return
# 	if n==2:
# 		return
# 	else:
# 		print ("%s->%s %s->%s %s->%s %s->%s"%(x,z,x,y,z,y,x,z))
# 		print ("%s->%s %s->%s %s->%s %s->%s"%(y,z,y,x,z,x,z,y))
		





		# if b=="c" and c=="a":
		# 	hano(n-1)



										# hano(target-2,a,c,b)

# hano(4,"a","b","c")
# hano(5,"a","b","c")
# hano(6,"a","b","c")









def hano_more():
	return

#brute_force
		










# hano(1,"x","y","z")
# hano(2,"x","y","z")
# hano_simple(2,"x","y","z")

#move plate x->y ,x->z,y->z x->y
#move plate z->x,z->y,x->y,x->z
#move plate y->x,

