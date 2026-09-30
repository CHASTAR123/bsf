class Graph():
    def __init__(self, n):
        self.n = n
        self.adj = [[]*n for i in range(n)]
    
    def create_edges(self, x, y):
        self.adj[x-1].append(y-1)
        self.adj[y-1].append(x-1)
    
    def bfs_traversel(self, source):
        visited = [False]*self.n
        rs = []
        queue = []
        queue.append(source)
        visited [source] = True
        while len(queue)> 0:
            s = queue.pop(0)
            s.append(rs)
            for i in self.adj[source]:
                if visited[source] == False:
                    i.append(queue)
                    visited[i] = True

