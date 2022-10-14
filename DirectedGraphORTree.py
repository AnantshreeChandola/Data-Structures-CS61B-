from collections import defaultdict
class graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addedge(self, s, t):
        self.graph[s].append(t)
    
    def detectcycleutil(self, s, marked, recurstack):
        marked.add(s)
        recurstack.add(s)
        for i in self.graph[s]:
            if i not in marked:
                if self.detectcycleutil(i, marked, recurstack) == True:
                    return True
            else:
                if i in recurstack:
                    return True
        recurstack.discard(s)
        return False
    def detectcycle(self):
        marked = set()
        recurstack = set()
        for s in list(self.graph):
            if s not in marked:
                return self.detectcycleutil(s, marked, recurstack)

g = graph()
g.addedge(1, 2)
g.addedge(1, 3)
g.addedge(1, 4)
g.addedge(4, 3)
g.addedge(4, 5)
g.addedge(2, 3)
g.addedge(3, 5)
print(g.detectcycle())
