TAX_RATE=0.1
import decimal
from math import sqrt
class Bet_tool():
	def __init__(self,arg):
		self.arg=arg
	def betrate_last(self,a,b):
		"输入两方的总投注额,计算小数点五位以后的概率(条件概率)"
		return round(b/a,5),round(a/b,5)
	def betrate_predict(self,pre_a,pre_b,a,b,amount,flag=None):
		#输入a方,b方某次(或多次)投注后的差值,和amount的总量,输出两方的投注额
		d1,d2=a-pre_a,b-pre_b
		if d1<0:
			true_b=amount/d2
			tmp=true_b*amount/abs(d1)
			true_a=sqrt(tmp+(amount/2)**2)-amount/2
			return true_a,true_b
		if d2<0:
			true_a=amount/d1
			tmp=true_a*amount/abs(d2)
			true_b=sqrt(tmp+(amount/2)**2)-amount/2
			return true_a,true_b
	def binomial_betrate(self):
		pass
	def bet(self):
		total=100
		b1,b2=0.95,0.95
		q_lose=0.5#不一定相加等于1
		p_lost=0.5#不一定相加等于1
		f=(b1*p-q)/b1
		print (total*f)
		return total*f
	def all():
		"所有的一切都是为了赌博的自由"
# from bs4 import BeautifulSoup

	#pre_a参数是下注前a方的赔率,pre_b是下注前b方的赔率,amount是你的投注量
	#print ("赔率之积为1",pre_a*pre_b)
	#print ("赔率之积为1",a*b)
	#true_b=amount/d2+amount
	# true_a=amount/d1+amount	
	#true_a=sqrt(tmp+(amount/2)**2)-amount/2

#    b的赔率(比例)差        a的赔率(比例)差       a增加 b不变   |   b增加 a不变  
# a1/b1-a2/b2=t1 b1/a1-b2/a2=t2 a2-a1=t3 (b1=b2)或 b2-b1=t3 (a1=a2)
# a1/b-(t3+a1)/b=t1 b/a1-b/(a1+t3)=t2 | a/b1-a/(t3+b1)=t1 b1/a-(t3+b1)/a=t2
# t3/b=t1 b/a1-b/(a1+t3)=t2 | t3/a=t2 a/b1-a/(t3+b1)=t1



#print (betrate_predict(pre_a,pre_b,a,b,4600))


# print ("二次前的值",17000/(20/12-37/12))
# print ("二次前的值",17000/(12/20-12/37))
# test1=17000/abs(20/12-37/12)
# test2=17000/abs(12/20-12/37)
# print ("计算错误",sqrt(test1+(17000/2)**2)-1117000/2)
# print ("计算错误",sqrt(test2+(17000/2)**2)-1117000/2)


#print (sqrt(27225)-15)

print(0.6-0.59701)
print(1.66667-1.675)
#连败的概率,连胜的概率,和概率论和信息论之间的交集
