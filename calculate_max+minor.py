match_table=[["Aster","Alliance"],["Gambit","BOOM"]]
set_origin=["Aster","Alliance","Gambit","BOOM"]
from algs_rc_nchoosek import *
round_one=multiple_set_rules_combination(match_table,[],0,[])




round_two=[]
for one in round_one:
	for ifmatch in round_one:
		if not set(one)&set(ifmatch):
			round_two.append([one,ifmatch])
print (round_two)
print ("-"*20)
for i in round_two:
	p=multiple_set_rules_combination(i,[],0,[])
	print (p)
	for j in p:
		for x in set(j)^set(set_origin):
			t=[j[0],x]
			print (t)
			for cham in t:
				print (cham)
	print ("=="*10)

t=[['Aster-Gambit','Alliance-BOOM'],['Aster-BOOM','Alliance-Gambit']]
# for i in round_one:


#print (set([1,2,2])&set([3,4,5]))

# 	for j in i:
# 		print (j+"-",end="")
# 	print ("")
"mainstage_minor"
