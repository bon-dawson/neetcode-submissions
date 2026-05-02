# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ans = []
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node:
                ans.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                ans.append('#')

        return ",".join(ans)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")

        if vals[0] == '#':
            return None

        root = TreeNode(int(vals[0]))
        q = deque([root])
        index = 1
        while q:
            node = q.popleft()
            if vals[index] != '#':
                node.left = TreeNode(int(vals[index]))
                q.append(node.left)
            index += 1
            if vals[index] != '#':
                node.right = TreeNode(int(vals[index]))
                q.append(node.right)
            index += 1
        return root