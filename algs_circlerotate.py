a,b="abca","cbaa"

def cr(a,b):
	assert len(a)==len(b),"长度不对,回环不行"
	for i in range(len(a)):
		if b.count(a[i])!=a.count(a[i]):
			return False
	return True
print (cr(a,b))


"1.计算一对等长字符串能否通过移动字符来形成对方的字符串 注意这对字符串一定是可逆的 也就是说a->b 等价于 b->a"
"2.计算有多少种移动方法?"
"3.最小的步骤是哪种方法?"

