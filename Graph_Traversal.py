from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def Addedge(self, s, t):
        self.graph[s].append(t)
    
    def Hasedge(self, s, t):
        for i in self.graph[s]:
            if i == t:
                return True
        else:
            return False

    def Dfsutil(self, v, marked):
        marked.add(v)
        print(v)
        for w in self.graph[v]:
            if w not in marked:
                Graph.Dfsutil(self, w, marked)
    def Dfs(self, v):
        marked = set()
        self.Dfsutil(v, marked)

    def Bfs(self, v):
        marked = set()
        queue = [v]
        marked.add(v)
        while queue:
            print(queue[0])
            s = queue.pop(0) 
            for w in self.graph[s]:
                if w not in marked:
                    queue.append(w)
                    marked.add(w)

        

g = Graph()
g.Addedge('A', 'B')
g.Addedge('A', 'C')
g.Addedge('B', 'C')
g.Addedge('C', 'D')
g.Addedge('D', 'A')
g.Addedge('D', 'B')
g.Addedge('B', 'A')
g.Dfs('A')
g.Bfs('A')


            
