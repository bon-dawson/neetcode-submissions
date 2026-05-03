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
    # def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    #     g = DSU(len(edges))
    #     for u, v in edges:
    #         if not g.union(u, v):
    #             return [u, v]
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        indegree = [0] * (n + 1)
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indegree[u] += 1
            indegree[v] += 1

        q = deque()
        for i in range(1, n + 1):
            if indegree[i] == 1:
                q.append(i)

        while q:
            node = q.popleft()
            indegree[node] -= 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 1:
                    q.append(nei)

        for u, v in reversed(edges):
            if indegree[u] == 2 and indegree[v]:
                return [u, v]

        return []