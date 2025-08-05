class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        ans=0
        temp = baskets.copy()
        for i in range (len(fruits)):
            for j in range (len(baskets)):
                if baskets[j]!=-1:
                    if fruits[i]<=baskets[j]:
                        baskets[j]=-1
                        break
        print(baskets)
        for b in baskets:
            if b!=-1:
                ans+=1
        return ans
