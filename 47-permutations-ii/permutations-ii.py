class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        op=[]
        ans =[]
        def getans(nums,op,ans):
            if len(nums)==0:
                ans.append(op)
                return
            s =set()
            for i in range (len(nums)):
                if nums[i] not in s :
                    s.add(nums[i])
                    newip=nums[0:i]+nums[i+1:]
                    newop=op+[nums[i]]
                    getans(newip,newop,ans)
        getans(nums,op,ans)
        return ans
        