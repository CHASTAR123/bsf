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
        # source = source - 1
        queue.append(source)
        visited [source] = True
        while len(queue)> 0:
            print(queue)
            s = queue.pop(0)
            rs.append(s)
            for i in self.adj[s]:
                print(i)
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        
        print(rs)
g = Graph(4)
g.create_edges(1, 2)
g.create_edges(2, 3)
g.create_edges(2, 4)
g.create_edges(3, 4)
print(g.adj)
g.bfs_traversel(2)

