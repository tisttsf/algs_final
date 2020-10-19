from algs_rc_nchoosek import funtion_nchoosek
from itertools import combinations
from re import compile,search

list=[6, 8, 9, 10, 50, 99, 111, 166, 199, 233, 299, 388, 399, 520, 599, 666, 699, 999, 1200, 2333, 3000, 3888, 3999, 4999, 5200, 6666, 8888, 9999, 10001, 13140, 13140, 18888, 19999, 19999, 21000, 28888, 30000, 66666]
list.sort()
print (list)
print (len(list))
"假设我送某个数,对方要送什么数或者什么数的组合才能超过我加的数?"
pattern=compile("\d+ \d+")

CURRENT_LIST_ME,UPPER_SUM,CURRENT_LIST_OPP=list[4:23],30000,list[25]

def calculate_potential():
	return 30000*5,30000*5
POTENTIAL,POTENTIAL_OPP=calculate_potential()
print (CURRENT_LIST_ME,len(CURRENT_LIST_ME))

e=input("两组实时数字:")
valid_or_not=search(pattern,e)
while valid_or_not:
	s1,s2=int(e.split(" ")[0]),int(e.split(" ")[1])
	for button_times in range(1,5):
		costlist_to_chooselowest=[]
		for my_sequence in funtion_nchoosek(CURRENT_LIST_ME,button_times,[],[]):
			my_output=sum(my_sequence)
			we=s1+my_output+POTENTIAL
			they=s2+POTENTIAL_OPP
			diff=we-they
			if my_output<=UPPER_SUM and diff>=0:
				costlist_to_chooselowest.append(my_sequence)
		sorted_output=sorted(costlist_to_chooselowest,reverse=False,key=sum)[:3]
		print (sorted_output)
	valid_or_not=search(pattern,e)
	e=input("两组实时数字:")
