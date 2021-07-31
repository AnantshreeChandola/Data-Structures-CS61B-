from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def Addedge(self, s, t):
        self.graph[s].append(t)

    def ShortestdistanceUtil(self, s, t, dist, pre):
        queue = [s]
        dist[s] = 0
        pre[s] = None
        while queue:
            previous = queue.pop(0)
            for next in self.graph[previous]:
                if (dist[next] == 0 or dist[next]>dist[previous]+1) and next!=s:
                    queue.append(next)
                    pre[next] = previous
                    dist[next] = dist[previous]+1
                    if next == t:
                        return True
        return False
    def PrintShortestPath(self, s, t):
        dist = defaultdict(int)
        pre = defaultdict(str)
        path = [t]
        if not self.ShortestdistanceUtil(s, t, dist, pre):
            print(False)
        else:
            while pre[t] != None:
                path.append(pre[t])
                t = pre[t]
            print(path[::-1])


g = Graph()
g.Addedge('A', 'B')
g.Addedge('A', 'C')
g.Addedge('B', 'E')
g.Addedge('E', 'D')
g.Addedge('E', 'D')
g.Addedge('C', 'D')
g.PrintShortestPath('A', 'D')

