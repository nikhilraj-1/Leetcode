class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        res=0
        cache = {}
        def dfs(r,c):
            if r>=row or c>=col or matrix[r][c]==0:
                return 0
            if (r,c) in cache :
                return cache[(r,c)]
            cache[(r,c)]=1+min(dfs(r+1,c),dfs(r,c+1),dfs(r+1,c+1))
            return cache[(r,c)]
        
        for i in range (row):
            for j in range(col):
                res+=dfs(i,j)
        return res
        