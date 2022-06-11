# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def LCA(node):
            if not node or node.val in (startValue, destValue): return node
            left, right = LCA(node.left), LCA(node.right)
            return node if left and right else left or right
        lca = LCA(root)
        ps, pd = 0, ""
        stack = [(lca, "")]
        while stack:
            node, path = stack.pop()
            if node.val == startValue: ps = len(path)
            if node.val == destValue: pd = path
            if node.left: stack.append([node.left, path + "L"])
            if node.right: stack.append([node.right, path + "R"])
        return "U" * ps + pd
        