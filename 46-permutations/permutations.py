class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans =[]
        def P(nums,start,ans):
            if start==len(nums)-1:
                ans.append(nums[:])
            s = set()
            for i in range (start,len(nums)):
                if nums[i] not in s :
                    s.add(nums[i])
                    nums[start],nums[i]=nums[i],nums[start]
                    P(nums,start+1,ans)
                    nums[start],nums[i]=nums[i],nums[start]

        P(nums,0,ans)
        return ans
        