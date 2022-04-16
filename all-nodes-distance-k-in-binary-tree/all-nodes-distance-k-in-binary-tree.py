# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        def dfs(root, parent=None):
            if not root:
                return None
            root.parent = parent
            dfs(root.left, root)
            dfs(root.right, root)
        dfs(root)
        
        q = collections.deque([(target, 0)])
        visited = {target}
        
        while q:
            if q[0][1] == k:
                return [node.val for node, level in q]
            node, level = q.popleft()
            for neighbor in [node.left, node.right, node.parent]:
                if neighbor and neighbor not in visited:
                    visited.add(neighbor)
                    q.append([neighbor, level+1])
        return []
        
        