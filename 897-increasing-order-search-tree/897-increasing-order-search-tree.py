# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        ans = self.output = TreeNode()
        def inorder(root):
            if root:
                inorder(root.left)
                self.output.right = TreeNode(root.val)
                self.output = self.output.right
                inorder(root.right)
        inorder(root)
        return ans.right