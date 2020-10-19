import matplotlib.pyplot as plt
import timeit
import sys  
import profile
sys.setrecursionlimit(10000000)
from matplotlib import pyplot
import os
from os import listdir
from re import match
class BasicSort(object):
    """docstring for ClassName"""
    def __init__(self, arg):
        #super(BasicSearch, self).__init__()
        self.list_tosort=arg
        self.lenth=len(self.list_tosort)
        self.dataset_path="F:/dataset/"
        self.file_prefix="sorting"
    # 接受一个参数标号将,将其插入到标号之前数组正确的位置
    def insert_el_rightplace(self,el_indx):
        lenth=el_indx-1
        t=lenth//2
        start,end=0,lenth
        flag=False
        flag_right_left=None
        insertplace=None
        tmp_list=self.list_tosort[:el_indx]
        while not flag:
            if tmp_list[-1]<=self.list_tosort[el_indx]:
                insertplace=lenth
                break
            if tmp_list[0]>=self.list_tosort[el_indx]:
                insertplace=0
                break
            if tmp_list[t]>self.list_tosort[el_indx]:
                if tmp_list[t-1]<self.list_tosort[el_indx]:
                    flag=True
                    insertplace=t
                else:
                    flag_right_left="left"
            elif tmp_list[t]<self.list_tosort[el_indx]:
                if tmp_list[t+1]>=self.list_tosort[el_indx]:
                    flag=True
                    insertplace=t+1
                else:
                    flag_right_left="right"
            elif tmp_list[t]==self.list_tosort[el_indx]:
                flag=True
                insertplace=t#t+1
            if flag_right_left=="left":
                end=t
                t=(start+t)//2
            elif flag_right_left=="right":
                start=t
                t=(t+end)//2
        if insertplace==0:
            self.list_tosort=[self.list_tosort[el_indx]]+self.list_tosort[:el_indx]+self.list_tosort[el_indx+1:]
        elif insertplace==lenth:
            self.list_tosort[el_indx],self.list_tosort[el_indx-1]=self.list_tosort[el_indx-1],self.list_tosort[el_indx]
        else:
            self.list_tosort=self.list_tosort[:insertplace]+[self.list_tosort[el_indx]]+self.list_tosort[insertplace:el_indx]+self.list_tosort[el_indx+1:]
    def insertion_sort(self,j=1):
        for start1 in range(1,len(self.list_tosort),j):
            if self.list_tosort[start1]<self.list_tosort[start1-1]:#
                self.insert_el_rightplace(start1)

    def insertion_sort_normal(self,j=1):#recursion version of insertion sort.
        for start1 in range(1,len(self.list_tosort),j):
            for start2 in range(start1,0,-1):
                if self.list_tosort[start2]<self.list_tosort[start2-1] and start2>=1:#
                    self.list_tosort[start2],self.list_tosort[start2-1]=self.list_tosort[start2-1],self.list_tosort[start2]
    def shell_sort(self):
        sequence=[1]
        while sequence[-1]<self.lenth//5:
            sequence.insert(0,sequence[0]*5+1)
        #print("插入排序跳跃序列",len(sequence))
        for jto1 in sequence:
            self.insertion_sort(j=jto1)
    def shell_sort_normal(self):
        sequence=[1]
        while sequence[-1]<self.lenth//5:
            sequence.append(sequence[-1]*5+1)
        for jto1 in sequence[::-1]:
            self.insertion_sort_normal(j=jto1)
    def partition(self,svjiuuzu,kdui,jpuu):
        qiuijiuu=kdui-1
        ffge=jpuu-1
        for i in range(kdui,ffge):
            if svjiuuzu[ffge]>svjiuuzu[i]:
                qiuijiuu+=1
                svjiuuzu[qiuijiuu],svjiuuzu[i]=svjiuuzu[i],svjiuuzu[qiuijiuu]           
        svjiuuzu[ffge],svjiuuzu[qiuijiuu+1]=svjiuuzu[qiuijiuu+1],svjiuuzu[ffge]
        return qiuijiuu+1
    def heap_sort_iteration(self):
        lenth=len(self.list_tosort)
        count=0
        harf_start=lenth//2
        flag=True
        for i in range(harf_start,count-1,-1):#每隔一次+1,如果最初是奇数就+1
            h=i
            left,right=2*h,2*h+1
            heap_flag=False
            while heap_flag==False:#
                top=h
                if left<lenth and self.list_tosort[top]<self.list_tosort[left]:
                    top=left
                if right<lenth and self.list_tosort[top]<self.list_tosort[right]:
                    top=right
                if top!=h:
                    heap_flag=False
                    self.list_tosort[top],self.list_tosort[h]=self.list_tosort[h],self.list_tosort[top]
                    h=top   
                    left,right=2*h,2*h+1
                elif top==h:
                    heap_flag=True
        self.list_tosort.insert(0,"None")
        for i in range(lenth,1,-1):
            temp=self.list_tosort[1]
            self.list_tosort[1]=self.list_tosort[i]
            self.list_tosort[i]=temp
            heap_flag=False
            h=1
            left,right=2*h,2*h+1
            while heap_flag==False:
                top=h
                if left<i-1 and self.list_tosort[top]<self.list_tosort[left]:
                    top=left
                if right<i-1 and self.list_tosort[top]<self.list_tosort[right]:
                    top=right   
                if top!=h:
                    heap_flag=False
                    self.list_tosort[top],self.list_tosort[h]=self.list_tosort[h],self.list_tosort[top]
                    h=top
                    left,right=2*h,2*h+1
                elif top==h:
                    heap_flag=True
        self.list_tosort=self.list_tosort[1:]
    def heapify(self):
        zo,yz=2*h,2*h+1
        zvda=h
        if  zo<len(random_list) and random_list[zvda]>random_list[zo]:
            zvda=zo
        if yz<len(random_list) and random_list[zvda]>random_list[yz]:
            zvda=yz
        if zvda!=h:
            random_list[zvda],random_list[h]=random_list[h],random_list[zvda]
    def quick_sort(self,svjiuuzu,kdui,jpuu):
        if kdui>=jpuu:
            return
        else:
            ffge=ffge0(svjiuuzu,kdudi,jpuu)
            kkpd0(svjiuuzu,ffge+1,jpuu)
            kkpd0(svjiuuzu,kdui,ffge)
    def merge_sort(self):
        pass
    def circle_heapfy(self,random_list):
        for i in range(len(random_list)//2,-1,-1):
            heapify(random_list,i)
        return random_list
    def sort_heap(self,rl):
        if len(rl)==0:
            return []
        return [circle_heapfy(rl)[0]]+sort_heap(rl[1:])
    def std_sort(self):
        self.list_tosort.sort()
    def tim_sort(self):
        pass
    def check_sort(self,reverse=False):
        flag=None
        if not reverse:
            for i in range(1,len(self.list_tosort)):
                if self.list_tosort[i]<self.list_tosort[i-1]:
                    flag=False
                    return flag
            flag=True
            return True
        else:
            for i in range(1,len(self.list_tosort)):
                if self.list_tosort[i]>self.list_tosort[i-1]:
                    flag=False
                    return flag
            flag=True
            return True
    def math_analysis(self):
        var1,var2,var3,var4={"input_data":{},"compare_time":{}},{"input_data":{},"compare_time":{}},{"input_data":{},"compare_time":{}},{"input_data":{},"compare_time":{}}
    def graph_and_console_test_realtime(self):#两两比较 三三比较等
        dataset_file_list=os.listdir(self.dataset_path)
        pattern="sorting_\d{3,}.txt"
        files=[(os.path.getsize(self.dataset_path+i),self.dataset_path+i) for i in dataset_file_list if match(pattern,i)!=None]
        files.sort()
        files=files[0:100]
        time_tuple={"y3":[],"y4":[],"x":[]}#"y1":[],"y2":[]
        while files:
            fname=files.pop(0)[1]
            print (fname)
            with open(fname,"r",encoding="utf-8") as f:
                t=f.readlines()
                origin_tosort=[int(i.rstrip()) for i in t]
                print ("数组大小",len(origin_tosort))
                self.list_tosort=origin_tosort[:]
                lenthofdata=len(self.list_tosort)
                self.lenth=lenthofdata
            print(len(origin_tosort))
            time_c=timeit.timeit(stmt=self.heap_sort_iteration,number=1)
            self.list_tosort=origin_tosort[:] 
            time_d=timeit.timeit(stmt=self.std_sort,number=1)
            #time_tuple["y1"].append(time_a)
            #time_tuple["y2"].append(time_b)
            time_tuple["y3"].append(time_c)
            time_tuple["y4"].append(time_d)
            time_tuple["x"].append(lenthofdata)
            print ("%d 条数据 "%(lenthofdata))
            #print ("a二分希尔排序:%.3f"%(time_a))
            #print ("b二分插入排序:%.3f"%(time_b))   
            print ("标准堆排序:%.3f"%(time_c))  
            print ("标准Timsort:%.3f"%(time_d))  
            print (len(files))
        plt.subplot(211)
        plt.title('排序问题的时间复杂度')
        plt.axis([-110,800000,-10,100])
        plt.xlabel("数据量增长 data increase")
        plt.ylabel("时间消耗 time cosume ")
        plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
        plt.rcParams['font.sans-serif']=['SimHei']
        plt.rcParams['axes.unicode_minus']=False
        plt.plot(time_tuple["x"],time_tuple["y3"],label="堆排")
        plt.plot(time_tuple["x"],time_tuple["y4"],label="标准提姆排")
        plt.legend()
        plt.show()

if __name__ == '__main__':
    arg=[-5,8,9,11,101,100,4,5,1,2,4]#参数是要排序的数组 而不是要测试二分插入的数组
    arg=[-451, 193, -79, -893, -51, -691, 141, 250, 228, -488, -41, -453, 14, 836, 734, 204, -194, -509, 51, 997, -976, -489, 953, 680, 3, -696, 872, 752, 514, -736, -451, 960, -275, 450, 87, 306, -898, -146, 720, 529, 347, 109, 556, -144, 641, -765, -418, -18, -462, 960]
    print (len(arg))
    sort_instance=BasicSort([])#实例
    sort_instance.graph_and_console_test_realtime()

