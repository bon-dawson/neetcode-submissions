class SegmentTree:
    def __init__(self, N, A):
        self.n = N
        self.build(N, A)

    def build(self, N, A):
        self.tree = [float("-inf")] * (2 * self.n)
        for i in range(N):
            self.tree[i + self.n] = A[i]
        for i in range(N - 1, 0, -1):
            self.tree[i] = max(self.tree[i << 1], self.tree[i << 1 | 1])

    def query(self, l, r):
        l += self.n
        r += self.n + 1
        ans = float("-inf")
        while l < r:
            if l & 1:
                ans = max(ans, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                ans = max(ans, self.tree[r])
            l >>= 1
            r >>= 1
        return ans

class Solution:
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     heap = []
    #     ans = []
    #     for i in range(len(nums)):
    #         heapq.heappush(heap, (-nums[i], i))
    #         if i >= k - 1:
    #             while heap[0][1] <= i - k:
    #                 heapq.heappop(heap)
    #             ans.append(-heap[0][0])
    #     return ans
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        st = SegmentTree(n, nums)
        ans = []
        for i in range(n - k + 1):
            ans.append(st.query(i, i + k - 1))
        return ans