class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        def monoinc(a1):
            for i in range(len(a1)-1):
                if a1[i]>=a1[i+1]:
                    return False
            return True
        for i in range(0,n-2*k+1):
            a1=nums[i:i+k]
            a2=nums[i+k:i+2*k]
            
            if monoinc(a1) and monoinc(a2):
                return True
        return False
        