# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.valid(float('-inf'),root,float('inf'))
    def valid(self,low,root,high)->bool:
        if not root:
            return True
        if not (low<root.val<high):
            return False
        return self.valid(low,root.left,root.val) and self.valid(root.val,root.right,high)
