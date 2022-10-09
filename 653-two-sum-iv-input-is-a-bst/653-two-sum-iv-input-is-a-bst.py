# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        output = []
        self.inorder(root, output)
        left, right = 0, len(output) - 1
        while left < right:
            nodeSum = output[left] + output[right]
            if nodeSum == k:
                return True
            elif nodeSum < k:
                left += 1
            else:
                right -= 1
        return False
    def inorder(self, node, output):
        if not node:
            return None
        if node.left:
            self.inorder(node.left, output)
        output.append(node.val)
        if node.right:
            self.inorder(node.right, output)