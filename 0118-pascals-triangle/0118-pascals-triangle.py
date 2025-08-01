class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        t = [[1]]
        for i in range (1,numRows):
            temp=[1]
            prev = t[i-1]
            for j in range(1,i):
                v = prev[j-1]+prev[j]
                temp.append(v)
            temp.append(1)
            t.append(temp)  
        return t

            
        