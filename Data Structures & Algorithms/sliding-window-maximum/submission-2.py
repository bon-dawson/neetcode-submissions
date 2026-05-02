class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        n = len(nums)
        mx_heap = []
        for r in range(n):
            if r >= k:
                ans.append(-mx_heap[0])

                if nums[r - k] == -mx_heap[0]:
                    heapq.heappop(mx_heap)

            heapq.heappush(mx_heap, -nums[r])

        ans.append(-mx_heap[0])

        return ans