from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def Addedge(self, s, t):
        self.graph[s].append(t)

    def Dfputil(self, s, marked, edgeto):
        marked.add(s)
        for i in self.graph[s]:
            if i not in marked:
                edgeto.append((s, i))
                self.Dfputil(i, marked, edgeto)
        return edgeto
    def Depthfirstpath(self, s):
        marked = set()
        edgeto = []
        print(self.Dfputil(s, marked, edgeto))

    def ShortestdistanceUtil(self, s, t, dist, pre):
        queue = [s]
        marked = set()
        marked.add(s)
        dist[s] = 0
        pre[s] = None
        while queue:
            previous = queue.pop(0)
            for next in self.graph[previous]:
                if next not in marked:
                    marked.add(next)
                    queue.append(next)
                    pre[next] = previous
                    dist[next] = dist[previous]+1
                    if next == t:
                        return True
        return False
    def PrintShortestPath(self, s, t):
        dist = {}
        pre = {}
        path = [t]
        self.ShortestdistanceUtil(s, t, dist, pre)
        while pre[t] != None:
            path.append(pre[t])
            t = pre[t]
        print(path[::-1])


g = Graph()
g.Addedge('A', 'B')
g.Addedge('A', 'C')
g.Addedge('B', 'C')
g.Addedge('C', 'D')
g.Addedge('D', 'A')
g.Addedge('D', 'B')
g.Addedge('B', 'A')
g.Depthfirstpath('A')
g.PrintShortestPath('A', 'D')

