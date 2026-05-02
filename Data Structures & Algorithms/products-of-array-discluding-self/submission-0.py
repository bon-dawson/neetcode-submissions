class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prod = 1
        ans = [1] * n
        for i in range(n):
            ans[i] *= prod
            prod *= nums[i]

        prod = 1
        for i in reversed(range(n)):
            ans[i] *= prod 
            prod *= nums[i]

        return ans