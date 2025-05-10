class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m = len(matrix[0])
        l,h=0,(n*m)-1
        while l<=h:
            mid = l +((h-l)//2)
            r = mid//m
            c = mid%m
            if matrix[r][c]<target:
                l=mid+1
            elif matrix[r][c]>target:
                h=mid-1
            else:
                return True
    
        return False
