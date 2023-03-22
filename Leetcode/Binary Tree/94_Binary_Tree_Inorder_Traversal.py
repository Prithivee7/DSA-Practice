# The below commented code is given by Leetcode itself

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ls = []
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            self.inorderTraversal(root.left)
            self.ls.append(root.val)
            self.inorderTraversal(root.right)
        return self.ls

# Better Solution
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        results = []
        def dfs(node):
            if node:
                dfs(node.left)
                results.append(node.val)
                dfs(node.right)
        dfs(root)
        return results