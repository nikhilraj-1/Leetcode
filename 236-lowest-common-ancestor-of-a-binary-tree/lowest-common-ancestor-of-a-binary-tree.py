# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root.val == p.val or root.val ==q.val:
            return root
        leftV = self.lowestCommonAncestor(root.left,p,q)
        rightV = self.lowestCommonAncestor(root.right,p,q)
        if leftV and rightV:
            return root
        if not leftV :
            return rightV
        return leftV