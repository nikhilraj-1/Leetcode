class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n = len(grid)
        def getCount(yv,ov):
            count =0
            for i in range (n):
                for j in range(n):
                    if (i==j and i<=(n//2) and j<=(n//2)) or (i+j==n-1 and i<=(n//2) and j>=(n//2) ) or (i>=n//2 and j == n//2):
                        if grid[i][j]!=yv:
                            count+=1
                    else:
                        if grid[i][j]!=ov:
                            count+=1
            return count
        return min (getCount(0,1),getCount(0,2),getCount(1,0),getCount(1,2),getCount(2,0),getCount(2,1))


        