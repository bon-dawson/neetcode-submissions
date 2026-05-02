# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ans = True
        def dfs(cur):
            if not cur:
                return 0
            
            left_height = dfs(cur.left)
            right_height = dfs(cur.right)

            if abs(left_height - right_height) > 1:
                self.ans = False

            return max(left_height, right_height) + 1
        
        dfs(root)
        return self.ans