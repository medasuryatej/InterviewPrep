# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 1
        def dfs(root):
            if not root:
                return 0
            left =  dfs(root.left)
            right = dfs(root.right)
            # left = max(left, 0)
            # right = max(right, 0)
            self.diameter = max(self.diameter, left + right + 1)
            return 1 + max(left, right)
        dfs(root)
        return self.diameter - 1