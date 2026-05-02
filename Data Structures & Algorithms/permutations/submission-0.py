class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(cur, vis):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return

            for i in range(len(vis)):
                if not vis[i]:
                    cur.append(nums[i])
                    vis[i] = True
                    dfs(cur, vis)
                    vis[i] = False
                    cur.pop()

        dfs([], [False] * len(nums))
        return res