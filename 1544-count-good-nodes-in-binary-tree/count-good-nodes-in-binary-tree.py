# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = self.dfs(root,root.val)
        return res

    def dfs(self, root: TreeNode, maxV)->int :
        if not root : return 0
        res =1 if root.val>=maxV else 0
        maxV = max(maxV,root.val)
        res+= self.dfs(root.left,maxV)
        res+= self.dfs(root.right,maxV)
        return res
        