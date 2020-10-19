start=list(range(100,1,-1))
start=[("c",[1,4,5]),("b",[1,2,5]),("c",[1,2,10,11,2])]
start.sort(key=lambda x:sum(x[1]))
print(start)

#根据时间排序
#根据文件大小排序
#根据信息熵排序
#根据概率排序
#根据点击数排序



k=lambda x:x[0]
print (k("cada"))
