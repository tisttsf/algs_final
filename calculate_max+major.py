from collections import namedtuple
from itertools import combinations
# from tkinter import *
from algs_rc_nchoosek import *
from re import findall,compile,search
match_rule={"GSL"}






dota_match_queue=["IG pg","NP j1","AF GF","C HR"]
type_12=["均","-1.5 ","+1.5","10+1","1+1","1+2","1+3","10+2","10+3","第一局","第二局","第三局"]
all_teams=[namedtuple("A","TNC Nigma Fnatic Aster"),namedtuple("B","VG Secret beastcoast Chaos"),namedtuple("C","IG RealityRift Alliance VP"),namedtuple("D","EG NaVi Liquid paiN")]
all_teams_dic={"A":["TNC","Nigma","Fnatic","Aster"],"B":["VG","Secret","beastcoast","Chaos"],"C":["IG","Reality","Alliance","VP"],"D":["EG","Navi","Liquid","paiN"]}

def team4(t):
    per={}
    for group in all_teams_dic:
        per[group]=[]
        for i in combinations(all_teams_dic[group],2):
            for x in t:
                afight=x.split(",")
                if afight[0] in i and afight[1] in i:
                    per[group].append(i)
                    break
    return per
def permutation_add_sequence(t):
    new=[]
    for i in t:
        tmp=[]
        for seq,j in enumerate(i):
            tmp.append((seq,j))
        new.append(tmp)
    return new
#给根据permutation_add_sequence a(胜者组序列),b(败者组序列) 根据 permutaion 序号
def helper(a,b):
    group_set_possible=[]
    for i in a:
        for j in b:
            list_to_string=[]
            for k,l in zip(i,j):
                if i.index(k)==1:
                    state="败者组"
                else:
                    state="胜者组"
                list_to_string.append(k+"-"+l+","+state)
            string="|".join(list_to_string)
            group_set_possible.append(string)
    return group_set_possible
def possble_sets_list(per):
    possble_sets=[]
    for group in per:
        possibles_pre=permutation_nonrepeated(per[group][0],2,[],[])
        possibles_latter=permutation_nonrepeated(per[group][1],2,[],[])
        a_group_set_possible=helper(possibles_pre,possibles_latter)
        tmp_list=[]
        for i in a_group_set_possible:
            two_teams_into_string=[]
            for j in i.split("|"):
                two_teams=j.split(",")[0].split("-")
                result=j.split(",")[1][0]
                two_team_result=[":".join([team,result]) for team in two_teams]
                two_teams_into_string.append(",".join(two_team_result))
            two_team_string="|".join(two_teams_into_string)
            tmp_list.append(two_team_string)
        possble_sets.append(tmp_list)
    all_results=multiple_rules_combination(possble_sets,[],0,[])
    return all_results


def helper_last(a,b):
    lastmatch_possibles={}
    for i in a:
        for j in b:
            last_match="-".join([i[1],j[0],"最后一轮"])     
            key="".join([i[1],"(败)"," ",j[0],"(胜)"])
            lastmatch_possibles[key]=last_match
    return lastmatch_possibles

def last_round_set(per):
    possible_lastmatch={}
    for group in per:
        possibles_pre=permutation_nonrepeated(per[group][0],2,[],[])
        possibles_latter=permutation_nonrepeated(per[group][1],2,[],[])
        lastmatch_possibles=helper_last(possibles_pre,possibles_latter)
        possible_lastmatch[group]=lastmatch_possibles
    return possible_lastmatch

def second_round():
    first_round_possibles=possble_sets_list(team4(t))
    second_round_group_sequence_possible={}
    for a_possible in first_round_possibles:
        a_possible_secondround_group={}
        for group_unit,group_symbol in zip(a_possible,["A","B","C","D"]):
            pattern=compile("\w+?(?=:)")
            team_sequence=findall(pattern,group_unit)
            upper,lower=tuple(team_sequence[:2]),tuple(team_sequence[2:])
            a_possible_secondround_group[group_symbol]=[upper,lower]
        second_round_group_sequence_possible[tuple(a_possible)]=last_round_set(a_possible_secondround_group)
    # print (len(second_round_group_sequence_possible))
    return second_round_group_sequence_possible
#a_possible_secondround_group是初始的第二轮对阵,需要1.用函数修饰并生成其结果的组合 2.打印结果"
#字典的(第一)键值是一轮过后胜负情况已分情况下,四个小组,所有可能的胜负情况和胜负情况后的对阵可能的组合1/256"
#键值是第二轮对阵情况后每(四)个小组都会根据第二轮的对阵的胜负结果再次对决组1组2的胜者败者对阵的所有可能情况1/256*1/256(每个小组有4种情况,同时又各自相对独立,所以1/4*1/4*1/4*1/4)"
#返回的是一个字典 层级为3 1级为第一轮所有可能的情况 2级为这种可能情况的小组号 3级为小组号的可能结果 16"
#group_stage_circumstance=second_round()
def last_round_combinations(group_stage_circumstance):
    combinations_last_round={}
    for r1_possible in group_stage_circumstance:
        last_possibles=[]
        for group in group_stage_circumstance[r1_possible]:
            items=list(group_stage_circumstance[r1_possible][group].values())
            last_possibles.append(items)
        last_possible_256=multiple_rules_combination(last_possibles,[],0,[])
        combinations_last_round[r1_possible]=last_possible_256
    return combinations_last_round
# f_nk(["胜","负"],4,[])
all_result=function_nchoosek(["胜","负","None"],15,[],[])
print(len(all_result))


#输入时一个可能序列的结果,判断有没有可能出现这种序列,可能出现这种序列就返回True,不可能发生就返回False
type_9=["均","-1.5 ","+1.5","10+1","10+2","10+3","第一局","第二局","第三局"]
def logical_filterfunction_9type(n):
    if n[0]=="None" or n[6]=="None" or n[7]=="None":#必然有胜负 必然打两场或以上
        return False
    if n[1]=="None" or n[2]=="None":
        return False
    if [n[6],n[7],n[8]].count(n[0])!=2:#三局必然是两局的结果跟1一样 而且是在条件1的基础上
        return False
    if n[8]=="None" and n[5]!="None":#
        return False
    if n[5]=="None" and n[8]!="None":#
        return False
    if n[8]=="None" and (n[1]!='负' or n[2]!='负') and n[5]=="None":
        return False
    if n[3]=="None" or n[4]=="None":#前两句十杀必然不是None 但是会是胜负的任意排列
        return False
    if n[1]=="胜" and n[0]!="胜":
        return False
    if n[2]=="胜" and n[0]!="负":
        return False
    return True


type_15=["均","-1.5","-2.5","+1.5","+2.5","10+1","10+2","10+3","10+4","10+5","第一局","第二局","第三局","第四局","第五局"]
print (len(type_15))
def logical_filterfunction_15type(n):
    if n[0]=="None" or n[6]=="None" or n[7]=="None":#必然有胜负 必然打三场或以上
        return False
    if n[1]=="None" or n[2]=="None":
        return False
    if [n[6],n[7],n[8]].count(n[0])!=2:#三局必然是两局的结果跟1一样 而且是在条件1的基础上
        return False
    if n[8]=="None" and n[5]!="None":#
        return False
    if n[5]=="None" and n[8]!="None":#
        return False
    if n[8]=="None" and (n[1]!='负' or n[2]!='负') and n[5]=="None":
        return False
    if n[3]=="None" or n[4]=="None":#前两句十杀必然不是None 但是会是胜负的任意排列
        return False
    if n[1]=="胜" and n[0]!="胜":
        return False
    if n[2]=="胜" and n[0]!="负":
        return False
    return True

#排除法将所有不可能出现的组合情况筛除(比如,A-1.5输则A-2.5不可能赢,A赢则B不可能赢)
def choose_result_by_rule():#type_9,type_8
    one_round_match_dic=[]
    for possible_result in all_result:
        if logical_filterfunction_9type(possible_result):
            triple_dic_format={}
            for one_result_part,key in zip(possible_result,type_9):
                triple_dic_format[key]=one_result_part
            one_round_match_dic.append(triple_dic_format)
    all_valid_result=len(one_round_match_dic)
    all_possible_result=len(all_result)
    return one_round_match_dic
choose_result_by_rule()

def convert_to_number(one_possible_result):
    triple_number_format=[]
    # print (type(one_possible_result))
    for i in one_possible_result:
        # print (i,one_possible_result[i])
        if one_possible_result[i]=="胜":
            triple_number_format.append(1)
        if one_possible_result[i]=="负":
            triple_number_format.append(0)
        if one_possible_result[i]=="None":
            triple_number_format.append(-1)
    return triple_number_format

#
bet_board=namedtuple("局","胜负 让一点五 受一点五 十杀1 十杀2 十杀3 第一局 第二局 第三局")
propability={}
for each_result in choose_result_by_rule():
    one_possible_result=convert_to_number(each_result)
    aresult=bet_board._make(one_possible_result)
    propability[aresult]={}

#more_combinations_of_group_stage=last_round_combinations(group_stage_circumstance)
#one_possible=more_combinations_of_group_stage[('Nigma:胜,Fnatic:胜|TNC:败,Aster:败', 'Secret:胜,beastcoast:胜|VG:败,Chaos:败', 'IG:胜,Alliance:胜|Reality:败,VP:败', 'Navi:胜,Liquid:胜|EG:败,paiN:败')]





#readable_dic(x)
#print (one_possible_result)
    # print (one_possible_result)
#one_round_match_list=[]
print ("全中的概率",256*256*104)
print ("54525952")