# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        inOrder = []
        self.inorder(root, inOrder)
        from collections import Counter
        modes_list = Counter(inOrder)
        # print(modes_list)
        most_common = modes_list.most_common(1)[0][1]
        # print(most_common)
        output = []
        for key, value  in modes_list.items():
            if value == most_common:
                output.append(key)
        return output
    def inorder(self, node, output):
        if not node:
            return None
        if node.left:
            self.inorder(node.left, output)
        output.append(node.val)
        if node.right:
            self.inorder(node.right, output)
            