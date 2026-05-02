class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        st = list(set(nums))
        n, ans = len(st), 1
        cnt = 1
        prev = st[0]
        for i in range(1, n):
            if st[i] - 1 == prev:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 1
            prev = st[i]
        return ans