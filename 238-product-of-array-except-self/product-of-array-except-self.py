class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=1
        zeroCount=0
        for i in range (len(nums)):
            if(nums[i]!=0):
                prod*=nums[i]
            else:
                zeroCount+=1
        res=[0]*len(nums)
        if zeroCount>1 :return res
        
        for i in range (len(nums)):
            if(zeroCount):
                res[i]=0 if nums[i]!=0 else prod
            else:
                res[i]=prod//nums[i]
        return res


        