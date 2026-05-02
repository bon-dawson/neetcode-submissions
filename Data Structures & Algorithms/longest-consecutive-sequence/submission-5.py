class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        i, n = 0, len(nums)
        ans = 0
        while i < n:
            if nums[i] - 1 not in st:
                length = 1
                while nums[i] + length in st:
                    length += 1
                ans = max(ans, length)
            i += 1

        return ans