import sys,io,itertools
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
def permutation_nonrepeated(t,m,cur,all_result):
	if m==0:
		d=cur[:]
		all_result.append(d)
		return
	for i in t:
		cur=cur+[i]
		permutation_nonrepeated(t[:t.index(i)]+t[t.index(i)+1:],m-1,cur)
		cur.remove(i)
def permutation_repeated(n,m,cur,all_result):
	if m==0:
		d=cur[:]
		all_result.append(d)
		return
	for i in n:
		cur=cur[:]+[i]
		permutation_repeated(n,m-1,cur,all_result)
		cur=cur[:-1]
	return all_result
def funtion_nchoosek(nelement_tofill,len_of_space,cur,all_result):
	if len(nelement_tofill)>len_of_space:
		all_result=permutation_repeated(nelement_tofill,len_of_space,[],[])
		return all_result
	remain=abs(len(nelement_tofill)-len_of_space)
	pre=permutation_repeated(nelement_tofill,len(nelement_tofill),[],[])
	last=permutation_repeated(nelement_tofill,remain,[],[])
	all_result=[]
	for i in pre:
		for j in last:
			all_result.append(i+j)
	return all_result


print (funtion_nchoosek(["火","冰","雷"],4,[],[]))

def subsequence():
	return 
def combinations():
	for j in itertools.combinations(["火","冰","雷"],2):
		print (j)
combinations()
