class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = -1
        i=0
        j = len(height)-1
        while i<j:
            ans =max(min(height[i],height[j])*(j-i),ans)
            if height[i]<height[j]:
                i=i+1
            else:
                j=j-1
        return ans
        