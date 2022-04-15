# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        # referred solution
        if not root:
            return root
        
        # low <= node.val <= right
        if (root.val >= low and root.val <= high):
            # need to trim both sides
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
        elif (root.val < low):
            # trim right side
            root = self.trimBST(root.right, low, high)
        elif (root.val > high):
            root = self.trimBST(root.left, low, high)
        else:
            pass
        return root