class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans = [0]*len(spells)
        
        for i in range(len(spells)):
            l=0
            h = len(potions)-1
            while(l<=h):
                m = (l+h)//2
                if (potions[m]*spells[i]>=success):
                    h=m-1
                else:
                    l=m+1
            ans[i]=len(potions)-h-1
        return ans

        