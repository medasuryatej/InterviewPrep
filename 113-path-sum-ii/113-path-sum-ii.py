# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.output = []
        def dfs(node, current, target):
            if not node:
                return
            if not node.left and not node.right:
                # print(current + [node.val])
                if sum(current + [node.val]) == target:
                    self.output.append(current + [node.val])
                return
            dfs(node.left, current+[node.val], target)
            dfs(node.right, current+[node.val], target)
        dfs(root, [], targetSum)
        return (self.output)