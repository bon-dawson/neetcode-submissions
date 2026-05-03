class DSU:
    def __init__(self, n):
        self.n = n
        self.p = list(range(n + 1))
        self.sz = [1] * (n + 1)
    
    def find(self, u):
        if u != self.p[u]:
            self.p[u] = self.find(self.p[u])
        return self.p[u]

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
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g = DSU(n)
        ans = n
        for u, v in edges:
            if g.union(u, v):
                ans -= 1
        return ans