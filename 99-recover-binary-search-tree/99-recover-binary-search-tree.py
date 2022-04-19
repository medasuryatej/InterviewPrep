# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        count = 2
        pred = None
        x = y = None
        while stack or root:
            # keep traversing left
            while root:
                stack.append(root)
                root = root.left
            # when no more left node
            # pop the stack top
            root = stack.pop()
            if pred and root.val < pred.val:
                y = root
                if not x:
                    x = pred
                else:
                    break
            # root is the predecessor to the next node
            pred = root
            # go right
            root = root.right
        x.val , y.val = y.val, x.val
            