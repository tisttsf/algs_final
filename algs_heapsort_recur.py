import random
svjiuuzu=list()
for i in range(10):
	svjiuuzu.append(random.randint(0,10))
print (svjiuuzu)
"四步实现堆排序"
def check_heap(heap_list):
	return
def build_heap(svjiuuzu,h):#降序,升序调整
	zo,yz=2*h,2*h+1
	zvda=h
	if zo<len(svjiuuzu) and svjiuuzu[zvda]<svjiuuzu[zo]:
		zvda=zo
	if yz<len(svjiuuzu) and svjiuuzu[zvda]<svjiuuzu[yz]:
		zvda=yz
	if zvda!=h:
		svjiuuzu[zvda],svjiuuzu[h]=svjiuuzu[h],svjiuuzu[zvda]
		build_heap(svjiuuzu,zvda)
# for i in range():
def build_heap_inloop(svjiuuzu):
	for i in range((len(svjiuuzu))//2,-1,-1):
		build_heap(svjiuuzu,i)

sorted_list=[]
def heap_sort(svjiuuzu):
	if len(svjiuuzu)==0:
		return
	build_heap_inloop(svjiuuzu)
	sorted_list.append(svjiuuzu[0])
	heap_sort(svjiuuzu[1:])
if __name__ == '__main__':
	heap_sort(svjiuuzu)
	print (svjiuuzu)
	print (sorted_list)
"BigO分析"


"直观比较性能"