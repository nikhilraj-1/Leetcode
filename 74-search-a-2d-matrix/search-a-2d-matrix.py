class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for i in range (len(matrix)):
            if matrix[i][0]<=target and target <=matrix[i][-1]:
                return self.binarySearch(matrix[i],target)
        return False

    def binarySearch(self,arr:List[int],target:int)->bool:
        l,h=0,len(arr)-1
        while l<=h:
            mid = l +((h-l)//2)
            if arr[mid]<target:
                l = mid+1
            elif arr[mid]>target:
                h=mid-1
            elif arr[mid]==target:
                return True
        return False
        