class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        mx_heap = [-w for w in stones]
        heapq.heapify(mx_heap)

        while mx_heap:
            fi = -heapq.heappop(mx_heap)
            if not mx_heap:
                return fi
            se = -heapq.heappop(mx_heap)

            if fi == se:
                continue
            heapq.heappush(mx_heap, - (fi - se))

        return 0