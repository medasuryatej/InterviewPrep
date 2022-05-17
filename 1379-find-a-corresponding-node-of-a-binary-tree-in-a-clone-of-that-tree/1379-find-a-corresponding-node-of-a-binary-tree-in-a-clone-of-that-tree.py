# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        # level order traversal
        # since values are unique when a node is equal to cloned - i get the expected output
        
        org = [original]
        cln = [cloned]
        
        for nd_o, nd_c in zip(org, cln):
            if nd_o.val == target.val:
                return nd_c
            for nd in (nd_o.left, nd_o.right):
                if nd != None:
                    org.append(nd)
            for nd in (nd_c.left, nd_c.right):
                if nd != None:
                    cln.append(nd)
        return None
        