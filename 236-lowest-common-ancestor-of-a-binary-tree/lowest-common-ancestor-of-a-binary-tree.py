# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path1,path2=[],[]
        self.findpath(root,p,path1)
        self.findpath(root,q,path2)
        ans = root
        for i in range (min(len(path1),len(path2))):
            if path1[i].val==path2[i].val:
                ans = path1[i]
        return ans
    def findpath(self, root:'TreeNode',n:'TreeNode',path:['TreeNode']):
        if not root:
            return False
        path.append(root)
        if root.val==n.val:
            return True
        if self.findpath(root.left,n,path) or self.findpath(root.right,n,path) :
            return True
               
        path.pop()