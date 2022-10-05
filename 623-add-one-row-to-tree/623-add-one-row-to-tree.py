# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, d: int, left: bool = True) -> Optional[TreeNode]:
        if d == 1:
            return TreeNode(val, root if left else None, root if not left else None)
        
        if root:
            root.left = self.addOneRow(root.left, val, d-1, True)
            root.right = self.addOneRow(root.right, val, d-1, False)
        return root