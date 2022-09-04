# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.wide = 0
        self.height = 0
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        cur_wide = 0
        cur_height = 0
        self.results = {}
        output = []
        self.updateWidthInorder(root, cur_wide, cur_height)
        # self.updateResultsDepthWise(root)
        for key in sorted(self.results.keys()):
            column = [i[1] for i in sorted(self.results[key])]
            output.append(column)
        return output
        
    def updateWidthInorder(self, node, cur_wide, cur_height):
        if node:
            node.wide = cur_wide
            node.height = cur_height
            if node.wide in self.results:
                self.results[node.wide].append((node.height, node.val))
            else:
                self.results[node.wide] = [(node.height, node.val)]
            self.updateWidthInorder(node.left, cur_wide-1, cur_height+1)
            self.updateWidthInorder(node.right, cur_wide+1, cur_height+1)
            
        