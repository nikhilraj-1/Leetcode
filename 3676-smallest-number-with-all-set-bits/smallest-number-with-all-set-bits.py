class Solution:
    def smallestNumber(self, n: int) -> int:
        p = 0
        ans = 1
        while(True):
            if 2**p >n:
                ans = 2**p
                break
            p +=1
        return ans-1