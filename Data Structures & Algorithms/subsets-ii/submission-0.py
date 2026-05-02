class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        def backtracking(cur, i):
            if i == len(nums):
                res.append(cur.copy())
                return

            cur.append(nums[i])
            backtracking(cur, i + 1)
            cur.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtracking(cur, i + 1)

        backtracking([], 0)
        return res