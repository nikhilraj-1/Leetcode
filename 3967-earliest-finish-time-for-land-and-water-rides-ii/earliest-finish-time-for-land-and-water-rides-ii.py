class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        #fix best land time
        ans = float('inf')
        blt = float('inf')
        for i in range (len(landStartTime)):
            blt = min(blt,landStartTime[i]+landDuration[i])
        for i in range(len(waterStartTime)):
            ans = min (ans, waterDuration[i]+max(blt,waterStartTime[i]))
        #fix best water time
        bwt = float('inf')
        for i in range(len(waterStartTime)):
            bwt = min(bwt,waterStartTime[i]+waterDuration[i])
        for i in range(len(landStartTime)):
            ans = min (ans,landDuration[i]+max(bwt,landStartTime[i]))
        return ans
