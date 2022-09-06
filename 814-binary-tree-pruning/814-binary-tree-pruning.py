# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return
            one_in_left = dfs(node.left)
            one_in_right = dfs(node.right)
            
            if not one_in_left:
                node.left = None
                
            if not one_in_right:
                node.right = None
                
            return node.val or one_in_left or one_in_right
        
        return root if dfs(root) else None