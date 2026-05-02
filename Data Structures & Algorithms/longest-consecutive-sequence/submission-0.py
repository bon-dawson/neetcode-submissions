class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        prev = float('-inf')
        cnt, ans = 0, 0
        for key in st:
            if key - 1 == prev:
                cnt += 1
            else:
                cnt = 1
            ans = max(ans, cnt)
            prev = key

        return ans