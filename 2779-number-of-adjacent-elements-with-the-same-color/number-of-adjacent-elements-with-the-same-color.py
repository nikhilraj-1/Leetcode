class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        nums, c = [0] * n, 0
        res=[]
        for index, color in queries:
            pre, nex = nums[index - 1] if index > 0 else 0, nums[index + 1] if index < n-1    else 0
            if nums[index] and nums[index] == pre: c -= 1
            if nums[index] and nums[index] == nex: c -= 1
            nums[index] = color
            if nums[index] == pre: c += 1
            if nums[index] == nex: c += 1
            res.append(c)
        return res
            