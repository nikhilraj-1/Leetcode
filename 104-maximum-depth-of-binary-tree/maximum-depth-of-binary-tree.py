# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [[root,1]]
        res=0
        while stack :
            node,n = stack.pop()
            res = max(res,n)
            if node.left:
                stack.append([node.left,n+1])
            if node.right:
                stack.append([node.right,n+1])  
        return res  

