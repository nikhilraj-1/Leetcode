class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        temp=[]
        res=[]
        currsum=0
        def dfs(i,currsum):
            if currsum==target:
                res.append(temp.copy())
                return
            if i>=len(candidates) or currsum>target:
                return
            temp.append(candidates[i])
            
            dfs(i,currsum+candidates[i])
            temp.pop()
            dfs(i+1,currsum)
        dfs(0,0)
        return res