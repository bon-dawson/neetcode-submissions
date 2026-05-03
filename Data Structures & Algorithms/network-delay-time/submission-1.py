class Solution:
    # def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    #     dist = [[float("inf")] * n for _ in range(n)]

    #     for u, v, t in times:
    #         dist[u - 1][v - 1] = t
    #     for i in range(n):
    #         dist[i][i] = 0

    #     for mid in range(n):
    #         for i in range(n):
    #             for j in range(n):
    #                 dist[i][j] = min(dist[i][j], dist[i][mid] + dist[mid][j])

    #     res = max(dist[k - 1])
    #     return res if res < float("inf") else -1
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float("inf")] * n
        dist[k - 1] = 0
        for _ in range(n - 1):
            for u, v, t in times:
                if dist[u - 1] + t < dist[v - 1]:
                    dist[v - 1] = dist[u - 1] + t
        max_dist = max(dist)
        return max_dist if max_dist != float("inf") else -1