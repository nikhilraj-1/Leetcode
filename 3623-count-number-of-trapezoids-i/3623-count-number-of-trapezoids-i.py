class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        hm ={}
        ans,total_sum = 0,0
        MOD = 10**9+7
        for p in points:
            hm[p[1]]=1+ hm.get(p[1],0)
  
        
        valid_counts = [y for y in hm.values() if y >= 2]
        if len(valid_counts)<2:
            return 0
        
        for p_num in hm.values():
            edge = p_num * (p_num - 1) // 2
            ans = (ans + edge * total_sum) % MOD
            total_sum = (total_sum + edge) % MOD
        return ans
        