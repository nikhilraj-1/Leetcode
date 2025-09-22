class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res =[]
        temp =[]
        def solve(i):
            if i>=len(s):
                res.append(temp[:])
                return
            for j in range(i,len(s)):
                if self.isPalin(s,i,j):
                    temp.append(s[i:j+1])
                    solve(j+1)
                    temp.pop()
        solve(0)
        return res

    def isPalin(self,s,i,j):
        while i<j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True

        