# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        que = []
        if root:
            que.append(root)
        else:
            return que
        result = []
        while que:
            curr_level, size = [], len(que)
            for i in range(size):
                each = que.pop(0)
                if each.left:
                    que.append(each.left)
                if each.right:
                    que.append(each.right)
                curr_level.append(each.val)
            result.append(curr_level)
        return result[::-1]