# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        inOrder = []
        self.inorder(root, inOrder)
        return inOrder == sorted(inOrder) and len(set(inOrder)) == len(inOrder)
    def inorder(self, node, output):
        if not node:
            return None
        if node.left:
            self.inorder(node.left, output)
        output.append(node.val)
        if node.right:
            self.inorder(node.right, output)