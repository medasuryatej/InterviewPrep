# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        hashTable = {}
        childset = set()
        root = None
        for description in descriptions:
            parent, child, isLeft = description
            if parent not in hashTable:
                hashTable[parent] = TreeNode(parent)
            if child not in hashTable:
                hashTable[child] = TreeNode(child)
            childset.add(child)
            if parent not in childset:
                root = parent
            if isLeft:
                hashTable[parent].left = hashTable[child]
            else:
                hashTable[parent].right = hashTable[child]
        # print(hashTable)
        return hashTable[(set(hashTable) - set(childset)).pop()]