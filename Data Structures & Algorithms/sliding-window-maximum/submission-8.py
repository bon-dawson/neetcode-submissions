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

    def update(self, p, value):
        p += self.n
        self.tree[p] = value

        while p > 1:
            self.tree[p >> 1] = max(self.tree[p], self.tree[p ^ 1])
            p >>= 1

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
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     n = len(nums)
    #     st = SegmentTree(n, nums)
    #     ans = []
    #     for i in range(n - k + 1):
    #         ans.append(st.query(i, i + k - 1))
    #     return ans
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        left_max, right_max = [0] * n, [0] * n
        left_max[0] = nums[0]
        right_max[n - 1] = nums[n - 1]
        for i in range(1, n):
            if i % k == 0:
                left_max[i] = nums[i]
            else:
                left_max[i] = max(left_max[i - 1], nums[i])

            j = n - 1 - i
            if j % k == 0:
                right_max[j] = nums[j]
            else:
                right_max[j] = max(right_max[j + 1], nums[j])

        ans = []
        for i in range(n - k + 1):
            ans.append(max(left_max[i + k - 1], right_max[i]))
        
        return ans