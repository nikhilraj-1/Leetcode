class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm={}
        for num in nums:
            hm[num]=1+hm.get(num,0)
        arr=[]
        for num,count in hm.items():
            arr.append([count,num])
        arr.sort(key = lambda x:x[0])

        res=[]
        while len(res)<k:
            res.append(arr.pop()[1])
        return res