def f(a_stock,amount,target):
	"calculate the target days"
	day=0
	while a_stock<=target:
		a_stock*=(1.04)
		day+=1
	return day

print (f(3.24,6300,8.764))

