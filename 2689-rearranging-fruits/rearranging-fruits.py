class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        freq = Counter(basket1)
        freq.subtract(Counter(basket2))
        rem = []
        amin = min(basket1+basket2)
        for i,f in freq.items():
            if f%2 !=0:
                return -1
            for k in range(abs(f)//2):
                rem.append(i)
        rem.sort()
        cost=0
        for i in range(len(rem)//2):
            c1 = rem[i]
            c2 = 2*amin
            cost+=min(c1,c2)
        return cost
        