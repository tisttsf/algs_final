class quick_find():
    def __init__(self,n):
        self.k=list(range(n))
        self.count=0
    def union(self,a,b):
        aid,bid=self.k[a],self.k[b]
        if aid==bid:
            self.count+=1
            return
        for i in range(len(self.k)):
            if self.k[i]==bid:
                self.k[i]=aid
        return self.k
    def find(self,a):
        return self.k[a]
class quick_union():
    def __init__(self,n):
        self.k=list(range(n))
        self.count=0
    def find(self,a):
        while a!=self.k[a]:
            a=self.k[a]
        return self.k[a]
    def union(self,a,b):
        r1,r2=self.find(a),self.find(b)
        if r1==r2:
            self.count+=1
            return True
        else:
            self.k[r1]=self.k[r2]
class weighted_union_find():
    def __init__(s,n):
        s.k=list(range(n))
        s.count=0
        s.sz=[1 for i in range(n)]
    def find(s,a):
        while a!=s.k[a]:
            a=s.k[a]
        return s.k[a]
    def union(s,a,b):
        r1,r2=s.find(a),s.find(b)
        if r1==r2:
            s.count+=1
            return 
        else:
            if s.sz[r2]>s.sz[r1]:
                s.k[r1]=s.k[r2]
                s.sz[r2]+=s.sz[r1]
            else:
                s.k[r2]=s.k[r1]
                s.sz[r1]+=s.sz[r2]
class pressed_union_find():
    def __init__(s,n):
        s.k=list(range(n))
        s.sz=[1 for i in range(n)]
        s.count=0
    def find(s,a):
        target=s.k[a]
        while a!=s.k[a]:
            a=s.k[a]
            s.k[a]=a
        return a
    def union(s,a,b):
        r1,r2=s.find(a),s.find(b)
        if r1==r2:
            return 
        else:
            s.k[r1]=s.k[r2]

"y1轴 y2轴 x轴"