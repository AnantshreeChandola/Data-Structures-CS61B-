class DisjointSets:
    def __init__ (self, nodes):
        self.parent = [i for i in range(nodes)]
        self.size = [1]*nodes
    def find(self, node): 
        pre = self.parent[node]
        while self.parent[pre] != pre:
            self.size[pre] -= self.size[node]
            pre = self.parent[pre]
        return pre
    def Isconnected(self, p, q):
        p = self.find(p)
        q = self.find(q)
        print(p, q)
        if (p == q):
            return True
        else:
            return False
    def Connect(self, p, q):
        p = self.find(p)
        q = self.find(q)
        if p == q:
            return
        else:
            if self.size[p] >= self.size[q]:
                self.parent[q] = p
                self.size[p] += self.size[q]
            elif self.size[q] > self.size[p]:
                self.parent[p] = q
                self.size[q] += self.size[p]



ds = DisjointSets(7)
ds.Connect(0, 2)
ds.Connect(2, 4)
ds.Connect(3, 1)
ds.Connect(5, 6)
print(ds.parent)
print(ds.size)
ds.Connect(0, 6)
ds.Connect(5, 1)
print(ds.Isconnected(0, 1))
print(ds.parent)
print(ds.size)
