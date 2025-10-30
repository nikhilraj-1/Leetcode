class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        n = len(target)
        count = target[0]
        for i in range(1,n):
            if target[i]>target[i-1]:
                count+= target[i]-target[i-1]

        return count
        