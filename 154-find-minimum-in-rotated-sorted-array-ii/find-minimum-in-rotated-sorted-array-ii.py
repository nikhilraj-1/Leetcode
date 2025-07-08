class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = sys.maxsize
        l,h=0,len(nums)-1
        while l<=h:
            m = (l+h)//2
            if nums[l]==nums[m]==nums[h]:
                ans = min(ans,nums[l])
                l+=1
                h-=1
            elif nums[l]<=nums[m]:
                ans = min(ans,nums[l])
                l=m+1
            else:
                ans = min(nums[m],ans)
                h=m-1
        return ans
        