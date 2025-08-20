class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row,col = len(matrix),len(matrix[0])
        dp =[]
        for _ in range (row):
            dp.append([0]*col)
        for r in range (row):
            dp[r][0]=matrix[r][0]
        for c in range (col):
            dp[0][c]=matrix[0][c]
        for i in range (1,row):
            for j in range(1,col):
                if matrix[i][j]==1:
                    dp[i][j] = 1 + min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
        ans =0
        for i in range (row):
            for j in range(col):
                ans += dp[i][j]

        return ans