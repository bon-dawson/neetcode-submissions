class DSU:
    def __init__(self, n):
        self.p = list(range(n + 1))
        self.sz = [1] * (n + 1)

    def find(self, u):
        if u == self.p[u]:
            return u
        return self.find(self.p[u])

    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u == v:
            return False
        if self.sz[u] < self.sz[v]:
            u, v = v, u
        self.sz[u] += self.sz[v]
        self.p[v] = u
        return True
        
        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        g = DSU(len(edges))
        for u, v in edges:
            if not g.union(u, v):
                return [u, v]