import heapq
"随机要排序的数组"
import random
random_list=list()
for i in range(10):
	random_list.append(random.randint(0,10))
random_list=[8, 8, 7, 10, 10, 1, 4, 10, 9, 5]
random_list=[1,2,3,4,5,6,7,8,9,10]

"四步实现堆排序"
##1.确定排序目标 2.从底建堆,从尾部循环建堆 3.根据堆特性排序
def heapify(random_list,h):
	zo,yz=2*h,2*h+1
	zvda=h
	if  zo<len(random_list) and random_list[zvda]>random_list[zo]:
		zvda=zo
	if yz<len(random_list) and random_list[zvda]>random_list[yz]:
		zvda=yz
	if zvda!=h:
		random_list[zvda],random_list[h]=random_list[h],random_list[zvda]
		heapify(random_list,zvda)
def circle_heapfy(random_list):
	for i in range(len(random_list)//2,-1,-1):
		heapify(random_list,i)
	return random_list
def sort_heap(rl):
	if len(rl)==0:
		return []
	return [circle_heapfy(rl)[0]]+sort_heap(rl[1:])
def heap():
	lenth=len(random_list)
	sorted_list=[]
	count=0
	harf_start=lenth//2
	flag=True
	for i in range(harf_start,count-1,-1):
		h=i
		left,right=2*h,2*h+1
		heap_flag=False
		while heap_flag==False:#
			top=h
			if left<lenth and random_list[top]>random_list[left]:
				top=left
			if right<lenth and random_list[top]>random_list[right]:
				top=right
			if top!=h:
				heap_flag=False
				random_list[top],random_list[h]=random_list[h],random_list[top]
				h=top	
				left,right=2*h,2*h+1
			elif top==h:
				heap_flag=True
	random_list.insert(0,"None")
	for i in range(lenth,1,-1):
		temp=random_list[1]
		random_list[1]=random_list[i]
		random_list[i]=temp
		heap_flag=False
		h=1
		left,right=2*h,2*h+1
		while heap_flag==False:
			top=h
			if left<i and random_list[top]>random_list[left]:
				top=left
			if right<i and random_list[top]>random_list[right]:
				top=right	
			if top!=h:
				heap_flag=False
				random_list[top],random_list[h]=random_list[h],random_list[top]
				h=top
				left,right=2*h,2*h+1
			elif top==h:
				heap_flag=True

def check_heap(r):
	pass


if __name__ == '__main__':
	print ("before",random_list)
	heap()
	print ("try:",random_list)
	random_list=[8, 8, 7, 10, 10, 1, 4, 10, 9, 5]	
	random_list=circle_heapfy(random_list)
	print (random_list)
	r=sort_heap(random_list)
	print(r)