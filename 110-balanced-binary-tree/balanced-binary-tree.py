# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.flag = True
        self.dfs(root)
        return self.flag

    def dfs(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        if abs(left - right) >1 :
            self.flag = False
        return 1 + max(left,right)
        