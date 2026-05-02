class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n):
            target = -nums[i]
            j, k = i + 1, n - 1
            while j < k:
                cur = nums[j] + nums[k]
                if cur > target:
                    k -= 1
                elif cur < target:
                    j += 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    break
        return ans