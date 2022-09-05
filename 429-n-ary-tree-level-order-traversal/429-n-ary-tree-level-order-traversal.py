"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:return []
        res = []
        stack = [root]
        while stack:
            temp = []
            next_stack = []
            for node in stack:
                temp.append(node.val)
                for child in node.children:
                    next_stack.append(child)
            stack = next_stack
            res.append(temp)
        return res