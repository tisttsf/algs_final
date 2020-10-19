"问题:1.json最底部的值字典转化为迭代 2.tkinter写的字典填写器"
from tkinter import *

c={'第一个': {'路径': {'深度': {'向左走,向右走': [1]}}}, '第二个': {'有些停滞了': {'深度学习': {'直走': [3], '探索': [3]}, '机器学习': {'继续探索': [3], '没法探索': [7]}, '深度机器学习': [7]}}, '第三个': [7], '第四个': [7], '第五个': {}}
SEQUENCES=[c]
b={1:2,2:3,4:5}

""""""
# def test_buttom(x):
def print_dic(a_dict,current_list,all_list):
	#判断最内部元素类型,如果是数值字符串(或其他)就直接append
	if type(a_dict) in [int,str]:
		current_list.append(a_dict)
		tmp=current_list[:]#将列表copy到一个新变量,不然append进all_list的列表会追踪为一个列表
		all_list.append(tmp)#临时变量
		current_list.pop(-1)#删除最后一个变量
	elif type(a_dict) in [tuple,list,set]:
		for last_element in a_dict:
			current_list=current_list+[last_element]
			tmp=current_list[:]#临时变量
			all_list.append(tmp)
			current_list.pop(-1)
	elif len(a_dict)==0:
		current_list.append(a_dict)
		tmp=current_list[:]#将列表copy到一个新变量,不然append进all_list的列表会追踪为一个列表
		all_list.append(tmp)#临时变量
		current_list.pop(-1)
	else:#没到底部就递归迭代字典
		for element in a_dict:
			current_list.append(element)
			print_dic(a_dict[element],current_list,all_list)
			current_list.remove(element)
	return all_list

def readable_dic(sequences):
	if len(sequences)==0:
		return 
	list_of_json=print_dic(sequences[0],[],[])
	for list in list_of_json:
		print ("->".join([str(element) for element in list]))#1.如果元素为数值则无法join,要转成字符串 2.字符串str后仍然是字符串
	print("-"*30)
	readable_dic(sequences[1:])
# print (print_dic(b,[],[]))
# readable_dic(SEQUENCES)
#readable_dic(SEQUENCES)

	#for i in a_dict:
#print_dic(d)


from json import load
filename="机器学习周.json"
with open(filename,"r",encoding="utf-8") as f:
	dic=load(f)
print (readable_dic([dic]))

