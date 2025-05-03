class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm={}
        for n in nums:
            hm[n]= 1+ hm.get(n,0)
        freq = [[] for i in range (len(nums)+1)]
        for n,c in hm.items():
            freq[c].append(n)
        res=[]
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res)==k:
                    return res


        