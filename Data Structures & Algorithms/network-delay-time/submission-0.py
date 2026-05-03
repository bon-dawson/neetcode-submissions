class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [[float("inf")] * n for _ in range(n)]

        for u, v, t in times:
            dist[u - 1][v - 1] = t
        for i in range(n):
            dist[i][i] = 0

        for mid in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][mid] + dist[mid][j])

        res = max(dist[k - 1])
        return res if res < float("inf") else -1