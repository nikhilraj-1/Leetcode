class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res = [0]*len(temp)
        stack = [] #(val,index)
        for i,n in enumerate(temp):
            while (stack and n>stack[-1][0]):
                val,idx = stack.pop()
                res[idx]=i-idx
            stack.append([n,i])
        return res    
            
        