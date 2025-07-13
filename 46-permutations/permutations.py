class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        op =[]
        ans =[]

        def permuatations(nums,op,ans):
            if len(nums)==0:
                ans.append(op)
                return
            s =set()    
            for i in range(len(nums)):
                if nums[i] not in s:
                    s.add(nums[i])
                    newIp=nums[0:i]+nums[i+1:]
                    newop=op+[nums[i]]
                    permuatations(newIp,newop,ans)
        permuatations(nums,op,ans)
        return ans
    
    


    