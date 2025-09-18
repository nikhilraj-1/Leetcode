class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        min_t = float('inf')
        for t in tasks:
            min_t = min (min_t, t[0]+t[1])
        return min_t
