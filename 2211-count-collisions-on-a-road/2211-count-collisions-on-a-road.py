class Solution:
    def countCollisions(self, directions: str) -> int:
        n = len(directions)
  
        leftL = 0
        while leftL < n and directions[leftL] == 'L':
            leftL += 1

        rightR = 0
        while rightR < n and directions[n - 1 - rightR] == 'R':
            rightR += 1

        countS = directions[leftL:n - rightR].count('S')
        
        return n - leftL - rightR - countS