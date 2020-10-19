def printList(l,layer=0):
    for k in l:
        if isinstance(k,list):
            printList(k,layer+1)
        else:
            print("--"*layer,k)
 

lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
printList(lis)