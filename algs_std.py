print (help(sorted))
s=sorted([[1,2],[1,3],[7,5],[3,4]],reverse=True,key=sum)

set_needtosort={"x":[2,5,6,7,8],"b":[2,4,5,1,3,1],"c":[2,3,5,6,8,9]}
def f(i):
	return sum(set_needtosort[i])/len(set_needtosort[i])
sorted(set_needtosort,reverse=True,key=set_needtosort)

class Sort_type(object):
	"""docstring for Sort_"""
	def __init__(self, arg):
		super(Sort_, self).__init__()
		self.arg = arg
	def sort_normal_number_list(self):
		return
	def sort_sum_list(self):
		return
	def sort_average_list(self):
		return
	def sort_len_list(self)
		return			
