# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res

        q = deque([root])
        while q :
            temp =[]
            for i in range (len(q)):
                v = q.popleft()
                if v:
                    temp.append(v.val)
                    q.append(v.left)
                    q.append(v.right)   
            if temp:            
                res.append(temp) 
        return res       
        