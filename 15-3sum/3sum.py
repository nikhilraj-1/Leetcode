class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i, n in enumerate(nums):
            l,r=i+1,len(nums)-1
            if n>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            while l<r:
                sum = n+nums[l]+nums[r]
                if sum>0:
                    r-=1
                elif sum<0:
                    l+=1
                else:
                    res.append([n,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return res
            

        