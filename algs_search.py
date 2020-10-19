#from dataset_1 import *
import sys
#try:
#    f=sys.argv[1]
#    l=readintolist(f)
#except:
#    l=generate()#generate normal test

class BasicSearch(object):
    """docstring for ClassName"""
    def __init__(self, arg):
        #super(BasicSearch, self).__init__()
        self.search_list = arg
    def insert_el_rightplace(self,el):
        lenth=len(self.search_list)
        t=lenth//2
        start,end=0,lenth
        flag=False
        flag_right_left=None
        insertplace=None
        while not flag:
            if self.search_list[-1]<=el:
                insertplace=lenth
                break
            if self.search_list[0]>=el:
                insertplace=0
                break
            if self.search_list[t]>el:
                if self.search_list[t-1]<=el:
                    flag=True
                    insertplace=t
                else:
                    flag_right_left="left"
            elif self.search_list[t]<el:
                if self.search_list[t+1]>=el:
                    flag=True
                    insertplace=t+1
                else:
                    flag_right_left="right"
            elif self.search_list[t]==el:
                flag=True
                insertplace=t#t+1
            if flag_right_left=="left":
                end=t
                t=(start+t)//2
            elif flag_right_left=="right":
                start=t
                t=(t+end)//2
        self.search_list=self.search_list[:insertplace]+[el]+self.search_list[insertplace:]
        return self.search_list
    def insertion_sort(self):
    	pass
    def binary_search_tree(self,el):
        return

if __name__ == '__main__':
    arg=list(range(1,30,3))
    a=BasicSearch(arg)
    t=a.insert_el_rightplace(4)
    print (t)





"有序列表的二分查找:三种形式"
counter=0
def binary_search(l,t,c):
    global counter
    mid=len(l)//2
    if l[mid]==t:
        return mid
    else:
        if l[mid]>t:
            c+=1
            return  binary_search(l[:mid],t,c)
        else:
            c+=1
            return binary_search(l[mid:],t,c)
"线性查找"
def linear_search(target):
    for i,j in enumerate(A):
        if t==i:
            return i,j

"二叉查找树(问题:如果我对有序表使用二叉查找树),对普通列表使用斐波那契查找,都不如查找复杂度,代码,图像,渐进分析,印在脑子里来的愉快"
def search(s,e,t):
    if e-s<=1:
        if A[s]==t:
            return A[s],s
        elif A[e]==t:
            return A[e],e
        else:
            return None
    mid=(s+e)//2
    if A[mid]==t:
        return A[mid],mid
    l=search(s,mid-1,t)
    if not l:
        r=search(mid+1,e,t)
        if not r:
            return None
        else:
            return r
    else:
        return l
def search_1(A,s,e,t):
    mid=(s+e)//2
    print (mid)
    if A[mid]==t:
        return A[mid],mid
    elif A[mid]>t:
        return search_1(A,s,mid,t)
    else:
        return search_1(A,mid,e,t)
"哈希表查找:优势,劣势,条件,时间复杂度计算"
