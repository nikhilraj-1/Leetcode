class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m= len(matrix)
        n = len(matrix[0])
        count =0

        def isValid(r,c,size):
            for i in range (r,r+size):
                for j in range(c,c+size):
                    if i >= m or j>=n or matrix[i][j]==0:
                        return False
            return True

        for i in range (m):
            for j in range (n) :
                if matrix[i][j]==1:
                    count+=1
                    size=2
                    while(isValid(i,j,size)):
                        count+=1
                        size+=1
        return count
        