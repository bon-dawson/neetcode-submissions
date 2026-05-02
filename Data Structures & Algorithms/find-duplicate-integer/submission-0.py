class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i, n = 0, len(nums)
        while i < n:
            if nums[i] == 0:
                i += 1
                continue
            if nums[nums[i] - 1] == 0:
                return nums[i]
            
            nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], 0