class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        if k == 0:
            return len(set(nums))
        intervals = [(x - k, x + k) for x in nums]
        intervals.sort(key=lambda t: t[1])  # sort by right endpoint
        last = -10**30
        res = 0
        for l, r in intervals:
            pos = max(last + 1, l)
            if pos <= r:
                res += 1
                last = pos
        return res
        