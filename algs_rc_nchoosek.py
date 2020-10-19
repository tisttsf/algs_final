import sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
#方块字与对称,字母与对称,外星语与对称,(工元素发现过程)
def dv_if():
    calendar,mission_compeltion,hand_ser=["u","v","w",],["x","z","s","丧偶|冬眠|瞬移|粉色是保护色|蓝色也是保护色吗|白色|绿色|色度|定义颜色|猥妻|尸检|视奸|苏远红,苏明玉|"],["苏铖兆|赵美兰|苏应培|苏想枝|曾清|汉克希望|苏**|苏*|苏辰|白银案之类的"]
    a,b,c=['1','2','3']#可改变对象,不可改变对象,他到底是编辑了自己还是用自己的双手编辑了其他物体成功后再让其编辑自己
    # xy,xx,t=["100x个基本粒子(看到|摸到|利用到)|恭喜你发现了新元素(反应)|同一时间你只能描述一件拉黑案"] #阴离子 银离子 引力子
print (dv_if())



def permutation_nonrepeated(t,m,cur,all_result):
    if m==0:
        d=cur[:]
        all_result.append(d)
        return
    for i in t:
        cur=cur+[i]
        permutation_nonrepeated(t[:t.index(i)]+t[t.index(i)+1:],m-1,cur,all_result)
        cur.remove(i)
    return all_result
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
#位选n
def function_nchoosek(nelement_tofill,len_of_space,cur,all_result):#
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


#集合互相搭配的可能情况[1,2...][a,b...][]
def multiple_set_rules_combination(set,possble_combination,n,cur):
    if n==len(set):
        d=cur[:]
        possble_combination.append(d)
        return
    else:
        for i in set[n]:
            cur.append(i)
            multiple_set_rules_combination(set,possble_combination,n+1,cur)
            cur.remove(i)
    return possble_combination



#leetcode优秀解法subsequence(完备解也有不完备,需要打乱)
def subsequence(nums):# def subsets(nums):
    """
    :param nums: List[int]
    :return: Set[tuple]
    """
    n = len(nums)
    total = 1 << n
    res = set()
    for i in range(total):
        subset = tuple(num for j, num in enumerate(nums) if i & 1 << j)
        res.add(subset)
    return res
c=subsequence([1,2,3,4,5,6])

"两种迭代方法"
def subsequence_iteration(L):
    List=[[]]
    for i in range(len(L)):
        for j in range(len(List)):
            List.append(List[j]+[L[i]])
    return List
def subsequence_combination(L):
    result_list=sum([List(map(list,combination(L,i))) for i in range(len(L)+1)],[])
    return result_list

"普通递归,代码量挺大,seed_list用来记录从第pre个开始计算子序列,islist是要每个都加入的子序列候选,cur是当前前缀子序列"
def subsequence_rc(total_list,seed_list,islist,cur,count,pre,flist,pre_in):
    #print (len(seed_list))
    # print (len(total_list))
    print (total_list)
    if len(seed_list)==0:
        return total_list
    if len(cur)==len(seed_list):
        #print (total_list)#
        # print (cur)
        count=0
        subsequence_rc(total_list,flist[pre+1:],flist[pre+1:][count+1:],flist[pre+1:][pre:count+1],count+1,pre+1,flist,pre_in)
    for i,j in enumerate(islist):
        tar=cur+[j]
        total_list.append(tar)
        if i==len(islist)-1:
            return subsequence_rc(total_list,seed_list,seed_list[count+1:],seed_list[pre_in]+seed_list[:count+1],count+1,pre,flist,pre_in)
# for i,j in enumerate([1,2,3]):
#   print (i,j)
# t=subsequence([],[1,2,3],[1,2,3],[],0,0,[1,2,3],0)
# print (t)
# t=subsequence([],[1,2,3,4],[1,2,3,4],[],0,0,[1,2,3,4],0)
# print (t)
# t=subsequence([],[1,2,3,4,5],[1,2,3,4,5],[],0,0,[1,2,3,4,5],0)
# print (t)
# t=subsequence([],[1,2,3,4,5,6],[1,2,3,4,5,6],[],0,0,[1,2,3,4,5,6],0)
# print (t)
def print_dic(a_dict,current_list,all_list):
    if type(a_dict)!=dict:#判断最内部元素类型,如果是数值字符串(或其他)就直接append
        if type(a_dict) in [int,str]:
            current_list.append(a_dict)
            tmp=current_list[:]#将列表copy到一个新变量,不然append进all_list的列表会追踪为一个列表
            all_list.append(tmp)#临时变量
            current_list.pop(-1)#删除最后一个变量
        elif type(a_dict) in [tuple,list]:
            for last_element in a_dict:
                current_list=current_list+[last_element]
                tmp=current_list[:]#临时变量
                all_list.append(tmp)
                current_list.pop(-1)
        return
    else:#没到底部就递归迭代字典
        for element in a_dict:
            current_list.append(element)
            print_dic(a_dict[element],current_list,all_list)
            current_list.remove(element)
    return all_list

def readable_dic(dic):
    list_of_json=print_dic(dic,[],[])
    for list in list_of_json:
        t="->".join([str(element) for element in list])
        if t.find("Nigma:胜")!=-1 and t.find("Navi:胜")!=-1 and t.find("IG:胜")!=-1 and t.find("Secret:胜")!=-1:
            if t.find("beastcoast:胜")!=-1 and t.find("Liquid:胜")!=-1 and t.find("Fnatic:胜")!=-1 and t.find("Alliance:胜")!=-1:
                print (t)

def dfs(g, s, v):
    # 递归结束条件
    if s in v:
        return v
    v.append(s)
    for i in range(len(g)):
        if i not in v and g[s][i]:
            v = dfs(g, i, v)
    return v
class Past():
    def __init__(self):
        pass
    def math_x(self):
        return
class GNERATION_FUNCTION(Past):#有规律的问题就是可接可实现的{可逆机}
    def __init__(self):
        a=["sys","清","helium","nitro"]
    def math_q():
        return 0
    def phy_q():
        return 0
    def che_q():
        return 0
    def bio_q():
        return 0
    def geo_q():
        return 0
    def social_q():
        return 0
    def war():
        return 0
    def DNA_q():
        return 0
   	def fq():
   		return


# 广度优先搜索 列表形式
def bfs(g, s):
    v = []
    q = []
    q.append(s)
    while q:
        s = q[0]
        q.remove(s)
        for i in range(len(g)):
            if i not in v and i not in q and g[s][i]:
                q.append(i)
        v.append(s)
    return v
if __name__ == '__main__':
    a=GNERATION_FUNCTION()
    print (a)