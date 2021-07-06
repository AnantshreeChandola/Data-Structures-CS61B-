class DisjointSets:
    def __init__ (self, nodes, parent):
        self.parent = [-1]*nodes
        self.size = [1]*nodes
    def Isconnected(self, p, q):
        while self.parent[p] >= 0:
            p = self.parent[p]
        while self.parent[q] >= 0:
            q = self.parent[q]
        if (p == q):
            return True
        else:
            return False
    def Connect(self, p, q):
        if not self.Isconnected(p, q):
            root = p if self.size[p] >= self.size[q] else q
            child = q if root == p else p
            while self.parent[child] >= 0:
                self.size[root] += self.size[child]
                self.size[self.parent[child]] -= self.size[child]
                curr = child
                child = self.parent[child]
                self.parent[curr] = root
            while self.parent[root] >= 0:
                root = self.parent[root]
            self.parent[child] = root
            self.size[root] += self.size[child]

ds = DisjointSets(11, [])
ds.Connect(0, 1)
ds.Connect(0, 2)
ds.Connect(0, 3)
ds.Connect(0, 4)
ds.Connect(0, 5)
ds.Connect(6, 7)
ds.Connect(6, 8)
ds.Connect(8, 9)
ds.Connect(9, 10)
print(ds.Isconnected(0, 7))
print(ds.parent)
print(ds.size)
ds.Connect(0, 8)
print(ds.parent)
print(ds.size)
print(ds.Isconnected(0, 7))

