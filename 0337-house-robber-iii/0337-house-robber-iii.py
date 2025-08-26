# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo={}
        def dfs(node):
            if not node :
                return 0
            if node in memo:
                return memo[node]
            rob_curr = node.val
            if node.left:
                rob_curr+=dfs(node.left.left)+dfs(node.left.right)
            if node.right:
                rob_curr+=dfs(node.right.left)+dfs(node.right.right)
            not_rob_curr = dfs(node.left)+dfs(node.right)
            memo[node]=max(rob_curr,not_rob_curr)
            return memo[node]
        return dfs(root)