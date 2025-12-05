class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)

        prefix[0]=nums[0]
        for i in range(1,len(nums)):
            prefix[i]= prefix[i-1]+nums[i]
        suffix[len(nums)-1]= nums[len(nums)-1]
        for i in range(len(nums)-2,-1,-1):
            suffix[i]=suffix[i+1]+nums[i]
        ans =0
        for i in range (0,len(suffix)-1):  
            if (prefix[i]-suffix[i+1])%2 ==0:
                ans+=1
        return ans   