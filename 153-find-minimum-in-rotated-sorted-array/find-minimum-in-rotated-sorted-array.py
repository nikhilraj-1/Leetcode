class Solution:
    def findMin(self, a: List[int]) -> int:
        ans = sys.maxsize
        l,h=0,len(a)-1
        while l<=h:
            mid = (l+h)//2
            if a[l]<=a[mid]:
                ans=min(a[l],ans)
                l=mid+1
            else:
                ans = min(a[mid],ans)
                h=mid-1

        return ans
            
        