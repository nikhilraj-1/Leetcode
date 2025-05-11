class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        res=0
        l,r=0,n-1
        lmax,rmax=height[0],height[n-1]
        while l<r:
            if lmax<=rmax:
                l+=1
                lmax=max(lmax,height[l])
                res+=lmax-height[l]
            else:
                r-=1
                rmax=max(rmax,height[r])
                res+=rmax-height[r]
        return res        