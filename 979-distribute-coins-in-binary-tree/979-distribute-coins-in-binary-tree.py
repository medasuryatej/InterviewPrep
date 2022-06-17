# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0
        def traverse(root):
            # none nodes dont need anything
            if not root: return 0
            # traverse left
            l = traverse(root.left)
            r = traverse(root.right)
            # irrespective of a node having excess coins or shortage
            # it contributes to the number of moves required
            self.moves += abs(l) + abs(r)
            # the baggage of current node is its value + leftsubtree + rightsubtree - 1
            # -1 here because thats is the minum value its should have, anything more is excess
            # under is shortage
            return root.val + l + r -1
        traverse(root)
        return self.moves