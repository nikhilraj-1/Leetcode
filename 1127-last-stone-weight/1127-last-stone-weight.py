class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq =[-s for s in stones]
        heapq.heapify(pq)
        while len(pq)>1:
            a = -heapq.heappop(pq)
            b = -heapq.heappop(pq)
            res = abs(a-b)
            if res:
                heapq.heappush(pq,-res)
        return -pq[0] if len(pq)>0 else 0
        