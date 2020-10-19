from random import randint


a={"1":{5:"jss",6:"jss",7:"jss",8:231},"2":{5:232,6:233,7:234,8:235},"3":{5:5,6:22,7:"xxx",8:236},"4":{5:"a",6:"b",7:"c",8:237}}
#print (a.values())
"我希望将其中的字符串全部转为数值赋值到b,其中原有数字保持不变"




"广度优先每次的深度要同步,但是传参该怎么传 才能保持同步深度 如果仅仅是for循环递归,name它会一直递归到深度的底部"
"需要用一个数组去追踪每层深度的节点的变量数"
"需要一个变量去追踪统一的深度?"
"变量传参数怎么传?"
class A():
	def __init__(self,a):
		self.a=a
	def __repr__(self):
		return str(self.a)
d2_m=[]
#for i in a:
#	cur.append(len(i))

b={}
a={1:{1:{1:{1:{2:{}}}}},3:4,5:6}
def f(same_depth_list,b,dep,cur_a,cur_b):
	if not same_depth_list:
		return
	for el_list in same_depth_list:
		for sub_el in el_list:
			key=A(sub_el)
			keyvalue={key:{}}
			b.update(keyvalue)
			if type(el_list[sub_el])==dict and len(el_list[sub_el])>0:
				for el in el_list[sub_el]:
					key=A(el)
					keyvalue={key:{}}
					#b[sub_el].update(keyvalue)
				cur_a.append(el_list[sub_el])
			elif el_list[sub_el]:
				key=A(el_list[sub_el])
				keyvalue={key:{}}
				cur_a.append(keyvalue)
	#此时b是一个字典对应着空值,我要在这个空值中加入对应长度的重复字典
	f(cur_a,b,dep+1,[],{})
f([a],b,0,[],{})#cur_b是一个空节点列表字段(绑定了对应key的)列表,cur_a是一个绑定了原始字典的同步深度的值列表字段,所以呢,因为我记录了每层深度的每个字段的长度,我将cur_b
"现在我不希望把广优的顺序,而是希望添加到其原有的位置,这可能需要cur_b来代替b的位置,并且每个节点的key或数量都要跟对"
print (b)

	#for i in b:
	#	for j in a[i]:
	#		if type(j)==str:
	#			key={ord(i):{}}
	#		elif type(j)==int:
	#			key={j:{}}
	#		b[i].update(key)


#f(a[i],b[i],[])
#f(a,b)

#	for j in b:
#		for k in d2_m:
#			b[j].update()
"对于所有的que我们迭代的传入这个que的元素的第一个然后删除它"