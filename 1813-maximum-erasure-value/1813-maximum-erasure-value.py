class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        s = set()
        i=0
        j=0
        res=0
        ans=0
        while j<(len(nums)):
            while nums[j] in s :
                s.remove(nums[i])
                res-=nums[i]
                i+=1
            s.add(nums[j])
            res+=nums[j]
            ans = max(res,ans)
            j+=1
        return ans

