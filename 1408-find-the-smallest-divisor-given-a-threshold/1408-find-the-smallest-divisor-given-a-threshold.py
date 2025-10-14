class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def calculateSum(divisor):
            return sum(math.ceil(num / divisor) for num in nums)
    
        left, right = 1, max(nums)
        
        while left < right:
            mid = (left + right) // 2
            if calculateSum(mid) <= threshold:
                right = mid
            else:
                left = mid + 1
        
        return left
        