class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def bt(nums, cur, i, n):
            if i == n:
                self.ans.append(cur.copy())
                return

            cur.append(nums[i])
            bt(nums, cur, i + 1, n)
            cur.pop()
            bt(nums, cur, i + 1, n)

            return

        bt(nums, [], 0, len(nums))
        return self.ans