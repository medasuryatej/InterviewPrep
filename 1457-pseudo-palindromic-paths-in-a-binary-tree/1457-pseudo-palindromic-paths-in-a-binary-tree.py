# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _isPesudoPalindrome(self, counter):
        oddFreq = False
        for num, freq in counter.items():
            if freq % 2 != 0:
                if not oddFreq:
                    oddFreq = True
                else:
                    return False
        return True
    
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.numPalindromes = 0
        # currentPath = []
        c = Counter()
        def dfs(node, counter):
            if not node:
                return None
            
            if not (node.left or node.right):
                # reached leaf node
                counter[node.val] += 1
                
                if self._isPesudoPalindrome(counter):
                    self.numPalindromes += 1
                    
                counter[node.val] -= 1
                return
            
            # add Node
            counter[node.val] += 1
            
            # traverse children
            dfs(node.left, counter)
            dfs(node.right, counter)
            
            # pop node
            counter[node.val] -= 1
            

        dfs(root, c)
        
        return self.numPalindromes