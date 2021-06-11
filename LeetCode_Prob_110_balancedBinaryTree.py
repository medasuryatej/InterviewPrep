# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check(root):
            # when u reach a leaf node there is nothing
            # beyond that, hence depth below that is zero
            if not root:
                return 0
            
            # check height of left tree
            left = check(root.left)
            # if left subtree is found to be imbalanced
            # no need to further check at rest
            if left == -1:
                return -1
            
            # check height of right tree
            right = check(root.right)
            # if right subtree is found to be imbalanced
            # no need to further check at rest
            if right == -1:
                return -1
            
            # when the height difference is more than 1
            # indicating it is not balanced hence return -1
            if abs(left - right) > 1:
                return -1
            
            # at every node increment depth by 1 and check 
            # maximum among depths of left subtree and right subtree
            return max(left, right) + 1
        
        return check(root) != -1