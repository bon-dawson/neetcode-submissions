class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = defaultdict(lambda: -1)
        n = len(nums)
        for i in range(n):
            if idx[target - nums[i]] != -1:
                return [idx[target - nums[i]], i]
            
            if idx[nums[i]] == -1:
                idx[nums[i]] = i