class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
    
        prev_gray = self.grayCode(n - 1)
        

        result = prev_gray[:]
        
        # Add reversed sequence with the nth bit set
        for i in range(len(prev_gray) - 1, -1, -1):
            result.append(prev_gray[i] | (1 << (n - 1)))
        
        return result
        