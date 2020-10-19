def create_hash(listforhash):
	hashtable_for_search={}
	for element in listforhash:
		hashtable_for_search[element]=1
	return hashtable_for_search
# assert len(h)==len(need_)
def bruteforce_whitelistproblem(target_set,filter_set):
	white_list=[]
	for special_element in target_set:
		if special_element in filter_set:
			white_list.append(special_element)
	return white_list

def brute_hashsearching(target_set,filter_set):
	advance_search_hashtable=create_hash(filter_set)
	white_list=[]
	for special_element in target_set:#a有重复 b没有重复
		if special_element in advance_search_hashtable:
			white_list.append(special_element)
	return white_list
def binary_searchtree():
	pass


def binary_search(start,end,target,search_list,counter):
	from math import log2
	mid=(start+end)//2
	if counter>=log2(len(search_list)):
		return None
	if search_list[mid]==target:
		return mid
	else:
		counter+=1
		if search_list[mid]>target:
			return	binary_search(start,mid,target,search_list,counter)
		elif search_list[mid]<target:
			return binary_search(mid,end,target,search_list,counter)
def sorting_and_binarysearch(target_elements,search_list):
	white_list,counter=[],0
	search_list.sort()
	start,end=0,len(search_list)-1
	for target_element in target_elements:
		index=binary_search(start,end,target_element,search_list,counter)
		if index:
			white_list.append(search_list[index])
	return white_list


class sorting():
	def __init__(self):
		pass
	def Timsort():
		return
	def Bucketsort():
		return
	def Toplesort():
		return
	def Heapsort():
		return
	def Mergesort():
		return
	def Quiksort():
		return
	def Shellsort():
		return
	def Basesort():
		return
    def coefficient():
        return




