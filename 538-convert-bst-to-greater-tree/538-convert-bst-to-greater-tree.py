# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.gsum = 0
    # nonlocal gsum
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        self.convertBST(root.right)
        self.gsum += root.val
        root.val = self.gsum
        self.convertBST(root.left)
        return root