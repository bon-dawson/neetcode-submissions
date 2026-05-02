class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)

        heap = []
        for num in cnt.keys():
            heapq.heappush(heap, (cnt[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans