class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        row,col = len(mat),len(mat[0])
        temp = [0]*col
        total=0

        def getRect(arr):
            count =0
            for i in range(len(arr)):
                minH= arr[i]
                for j in range (i,len(arr)):
                    minH = min(minH,arr[j])
                    count+=minH
            return count



        for i in range (row):
            for j in range (col):
                if mat[i][j]==1:
                    temp[j]+=1
                else:
                    temp[j]=0
            total+=getRect(temp)
        return total
                

        