class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        min_left = [0] * len(nums)
        max_right = [0] * len(nums)
        

        max_heap = []
        current_sum = 0
        
        for i in range(len(nums)):
            heapq.heappush(max_heap, -nums[i])  
            current_sum += nums[i]
            
            if len(max_heap) > n:

                removed = -heapq.heappop(max_heap)
                current_sum -= removed
            
            min_left[i] = current_sum
        

        min_heap = []
        current_sum = 0
        
        for i in range(len(nums) - 1, -1, -1):
            heapq.heappush(min_heap, nums[i])
            current_sum += nums[i]
            
            if len(min_heap) > n:
            
                removed = heapq.heappop(min_heap)
                current_sum -= removed
            
            max_right[i] = current_sum

        min_diff = float('inf')
        
        for i in range(n - 1, 2 * n):

            diff = min_left[i] - max_right[i + 1]
            min_diff = min(min_diff, diff)
        
        return min_diff
        