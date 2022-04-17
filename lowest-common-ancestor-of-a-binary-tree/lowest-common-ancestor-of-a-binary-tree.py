# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root):
            if not root:
                return False
            leftSide = dfs(root.left)
            rightSide = dfs(root.right)
            current = root == p or root == q
            if leftSide + rightSide + current >= 2:
                self.ans = root
                # return
            return current or leftSide or rightSide
        dfs(root)
        return self.ans
        