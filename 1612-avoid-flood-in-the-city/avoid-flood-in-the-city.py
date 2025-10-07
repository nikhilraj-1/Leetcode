class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [-1] * n
        last_full = {}           
        dry_days = []            
        for i, lake in enumerate(rains):
            if lake == 0: 
                ans[i] = 1
                dry_days.append(i)
            else:
                if lake in last_full:
                    j_pos = bisect_right(dry_days, last_full[lake])
                    if j_pos == len(dry_days):
                        return []  
                    j = dry_days.pop(j_pos)
                    ans[j] = lake
                last_full[lake] = i
                ans[i] = -1
        return ans
        