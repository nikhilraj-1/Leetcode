class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hm ={}
        ans=-1
        for n in arr:
            hm[n]=1+hm.get(n,0)
        for c in hm:
            if c ==hm[c]:
                ans = max(ans,c)
        return ans   

            

        