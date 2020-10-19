"快速排序"
def ffge0(b,p):
    jnhr=-1
    for i in b:
        if b[p]>i:
            jnhr+=1
            b[b.index(i)],b[jnhr]=b[jnhr],b[b.index[i]]
    b[p],b[jnhr+1]=b[jnhr+1],b[p]
    return jnhr+1
def kkpd0(b):
    if len(b)<=1:
        return b[0]
    else:
        p=ffge0(b)
        return kkpd0(b[p:])+kkpd0(b[:p])


"堆排序"



"归并排序"


"希尔排序"



"在基础排序上改进的排序"


"自己探索最优的排序"


"插入排序"
b=[3,4,1,1,10,20,30,50,60,90]
k=len(b)
def insertion_sort(n,m):#recursion version of insertion sort.
    if n==k:
        return 
    if m==0:
        return
    if b[m]>b[m-1] and m>=1:#
        b[m],b[m-1]=b[m-1],b[m]
        insertion_sort(n,m-1)
    if b[n]>=b[m]:
        insertion_sort(n+1,n+1)
def insertion_sort_():
    pass

insertion_sort(1,1)
print (b)






