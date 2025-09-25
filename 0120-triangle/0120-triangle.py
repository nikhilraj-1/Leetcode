class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp=[[float('inf')]*len(triangle[i]) for i in range(len(triangle))]
        def dfs(i,j):
            if i == len(triangle)-1:
                dp[i][j]=triangle[i][j]
                return dp[i][j]
            if dp[i][j] !=float('inf'):
                return dp[i][j]
            left = dfs(i+1,j)
            right =dfs(i+1,j+1)
            dp[i][j]=triangle[i][j] + min(left,right)
            return dp[i][j]
        return dfs(0,0)