class Solution:
    def maxSum(self, nums: List[int]) -> int:
        s = set()
        maxno = float('-inf')
        for n in nums :
            maxno = max(n,maxno)
            if n not in s :
                s.add(n)
        if maxno<0:
            return maxno
        ans =0
        for n in s:
            if n>0:
                ans+=n
        return ans

        