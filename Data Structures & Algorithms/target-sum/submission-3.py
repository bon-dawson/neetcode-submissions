class Solution:
    # def findTargetSumWays(self, nums: List[int], target: int) -> int:
    #     n = len(nums)
    #     ans = 0
    #     i = 0
    #     while i < (1 << n):
    #         current = 0
    #         for j in range(n):
    #             if (1 << j) & i:
    #                 current -= nums[j]
    #             else:
    #                 current += nums[j]
            
    #         if current == target:
    #             ans += 1

    #         i += 1
    #     return ans

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(n):
            for total, count in dp[i].items():
                dp[i + 1][total + nums[i]] += count
                dp[i + 1][total - nums[i]] += count

        return dp[n][target]