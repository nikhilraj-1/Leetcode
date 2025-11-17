class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        count =0
        first =True
        for i in range(len(nums)):
            if nums[i]==1 and i>0 and not first:
                if count <k:
                    return False
                count =0
            elif nums[i]==1 and first:
                first = False
                count =0
                
            else:
                count+=1
        return True

        