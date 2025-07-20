class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=set()
        temp=[]
        nums.sort()
        def dfs(i):
            if i>=len(nums):
                res.add(tuple(temp.copy()))
                return
            temp.append(nums[i])
            dfs(i+1)
            temp.pop()
            dfs(i+1)

        dfs(0)
        return list(res)    