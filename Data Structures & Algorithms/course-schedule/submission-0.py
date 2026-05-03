class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indegree = [0] * (n)
        for a, b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1

        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        while q:
            node = q.popleft()
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        for i in range(n):
            if indegree[i] != 0:
                return False

        return True