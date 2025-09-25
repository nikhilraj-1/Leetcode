class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
  
        res = [[0] * len(triangle[i]) for i in range(len(triangle))]
        res[0]=triangle[0]
        for i in range(1,len(triangle)):
            for j in range(len(triangle[i])):
                if j ==0:
                    res[i][j] = triangle[i][j] + res[i-1][j]
                elif j == len(triangle[i])-1:
                    res[i][j] = triangle[i][j]+res[i-1][j-1]
                else:
                    res[i][j]=triangle[i][j] + min(res[i-1][j],res[i-1][j-1])
        return min(res[len(triangle)-1])

        

        