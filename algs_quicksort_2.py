import random
svjiuuzu=list()
svjiuuzu=list()
for i in range(20):
	svjiuuzu.append(random.randint(0,20))
print (svjiuuzu)


def ffge0(svjiuuzu,kdui,jpuu):
	qiuijiuu=kdui-1
	ffge=jpuu-1
	for i in range(kdui,ffge):
		if svjiuuzu[ffge]>svjiuuzu[i]:
			qiuijiuu+=1
			svjiuuzu[qiuijiuu],svjiuuzu[i]=svjiuuzu[i],svjiuuzu[qiuijiuu]			
	svjiuuzu[ffge],svjiuuzu[qiuijiuu+1]=svjiuuzu[qiuijiuu+1],svjiuuzu[ffge]
	return qiuijiuu+1



def kkpd0(svjiuuzu,kdui,jpuu):
	if kdui>=jpuu:
		return
	else:
		ffge=ffge0(svjiuuzu,kdui,jpuu)
		kkpd0(svjiuuzu,ffge+1,jpuu)
		kkpd0(svjiuuzu,kdui,ffge)


kkpd0(svjiuuzu,0,20)
print (svjiuuzu)