# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.best = float("-inf")
    def maxPathSum(self, root):
        self._maxPathSum(root)
        return self.best
    def _maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self._maxPathSum(root.left)
        right = self._maxPathSum(root.right)
        left = max(left, 0)
        right = max(right, 0)
        self.best = max(self.best, left + right + root.val)
        return max(left, right) + root.val