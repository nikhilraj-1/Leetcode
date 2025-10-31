class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        s = Counter(nums)
        ans = []
        for k in s :
            if s[k]==2:
                ans.append(k)
        return ans
        