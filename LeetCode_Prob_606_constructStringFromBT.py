# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: TreeNode) -> str:
        if not root:
            return ""
        if root.left is None and root.right is None:
            return "{}".format(root.val)
        elif root.right is None:
            return "{}({})".format(root.val, self.tree2str(root.left))
        elif root.left is None:
            return "{}()({})".format(root.val, self.tree2str(root.right))
        else:
            return "{}({})({})".format(root.val, self.tree2str(root.left), self.tree2str(root.right))