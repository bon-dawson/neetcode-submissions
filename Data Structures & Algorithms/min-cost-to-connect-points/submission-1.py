class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.sz = [1] * n

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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        min_heap = []
        for i in range(n):
            xi, yi = points[i]
            for j in range(i + 1, n):
                xj, yj = points[j]
                min_heap.append((abs(xi - xj) + abs(yi - yj), i, j))

        heapq.heapify(min_heap)

        g = DSU(n)
        ans = 0

        while min_heap:
            w, i, j = heapq.heappop(min_heap)

            if g.union(i, j):
                ans += w
            
        return ans