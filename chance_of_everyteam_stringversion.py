import collections,string,re
print(dir(collections))
symbols="OmegaBigOBigThetaPolynomialPascal周鸿祎巨婴经济学杨舒然饕餮刘强东马化腾郭梦雅郭梦宇刘冬儿楚云飞罗文轩伍子胥车轴车胄李云龙理性让你清楚地知道你是错的感性让你不屑一顾的将错就错:氢氦锂钹碰铁钴镍磷砷铅铟铝汞镉锌金银铜铂"




City=collections.namedtuple("Geo",('name country population coordinates block'))#physical
Gamble=collections.namedtuple("Inf",('players score penaly shot key_pass mid_way break_way lease attack_penalty red_card'))#practical
Live=collections.namedtuple("Hot",('name province city weather tempreture humidity dry present'))
Play=collections.namedtuple("Col",('name skill state own looking'))
country=["马来西亚","伊朗","科威特","澳大利亚","叙利亚","中国","日本","乌兹别克斯坦","阿曼","卡塔尔","韩国","吉尔吉斯斯坦","约旦","伊拉克","土库曼斯坦","沙特阿拉伯","菲律宾","阿联酋","关岛","新加坡","马尔代夫","泰国","也门","塔吉克斯坦","黎巴嫩","越南","柬埔寨","蒙古","缅甸","朝鲜","孟加拉国","巴勒斯坦","巴林","中国香港","印度尼西亚","印度","阿富汗","尼泊尔","中国台北","斯里兰卡"]
list_flag=["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
#print (len(country))
#print (len(list_flag),end="\n")
list_City=[]

for i in country:#,j,k,l,p,o
   list_City.append(City(None,i,None,None,None))#list is a more advanced data structure that is way more advance than linear,list,queue,tuple

c=[i.country for i in list_City]
print (c)





#print(type(City),type(Gamble))
program={"":"","":"","":"","":"","":"","":"","":"","":"","":"","":"","":"","":"","":"","":"","":""}
score={}
penalty={}
shot={}
key_pass={}
mid_way={}
break_cast={}
lease_={}
attack_={}
red_card={}
yellow_card={}


