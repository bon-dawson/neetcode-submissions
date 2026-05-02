class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0
        i = 0
        while i < (1 << n):
            current = 0
            for j in range(n):
                if j & i:
                    current -= nums[j]
                else:
                    current += nums[j]
            
            if current == target:
                ans += 1

            i += 1
        return ans