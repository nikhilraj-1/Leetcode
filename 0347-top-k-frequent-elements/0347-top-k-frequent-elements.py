class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm={}
        for num in nums:
            hm[num]=1+hm.get(num,0)
        heap=[]
        for n in hm.keys():
            heapq.heappush(heap,[hm[n],n])
            if len(heap)>k:
                heapq.heappop(heap)
        res=[]
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
    