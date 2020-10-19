a={"a":5,"b":5,"c":5,"d":5,"k":5}
b={i:2 for i in "abcdk"}
c={i:100 for i in "abcd"}
c["k"]=2
from math import log
print (log(1/4,2))
class Impurity():
	def __init__(self,arg):
		self.arg=arg
		self.lenth=sum(self.arg.values())
		# self.gini=self.gini()
		# self.entropy=self.entropy()
	def gini(self):
		p_sum=0.0
		for i in self.arg:
			p1=self.arg[i]/self.lenth
			for j in self.arg:
				if i!=j:
					p2=self.arg[j]/self.lenth
					p_sum+=p1*p2
		return p_sum
	def entropy(self):
		entropy=0
		for i in self.arg:
			p=self.arg[i]/self.lenth
			entropy-=(p*log
			(p,2))
		return entropy
#随机投掷,进错的概率
print (Impurity(c).gini())
print (Impurity(a).entropy())
