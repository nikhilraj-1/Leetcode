class Solution:
    def rob(self, nums: List[int]) -> int:
        a = nums[0]
        if len(nums)<2:
            return a
        b = max(nums[0],nums[1])
        if len(nums)<3:
                return b
        def rob_l(nums):
            a = nums[0]
            if len(nums)<2:
                return a
            b = max(nums[0],nums[1])
            if len(nums)<3:
                return b
            for i in range (2,len(nums)):
                c = max(a+nums[i],b)
                a=b
                b=c
            return c
        c1=rob_l(nums[:-1])
        c2=rob_l(nums[1:])
        return max(c1,c2)
        