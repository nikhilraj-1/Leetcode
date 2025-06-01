# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0
        self.ans = None
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k(root,k)
        return self.ans
    
    def k(self,root,k):
        if not root or self.ans is not None:
            return 
        self.k(root.left,k)
        self.count+=1
        if self.count==k:
            self.ans= root.val
            return
        self.k(root.right,k)
        