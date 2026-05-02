class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        THRESHOLD = 10**5
        ans = []
        n = len(nums)
        mx_heap = []
        for r in range(n):
            if r >= k:
                ans.append(-mx_heap[0] - THRESHOLD)

                if nums[r - k] + THRESHOLD == mx_heap[0]:
                    heapq.heappop(mx_heap)
            
            heapq.heappush(mx_heap, - (nums[r] + THRESHOLD))

        ans.append(-mx_heap[0] - THRESHOLD)

        return ans