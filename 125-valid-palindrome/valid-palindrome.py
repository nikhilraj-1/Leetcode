class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s= re.sub(r'[^a-z0-9]','',s)
        l=0
        r=len(s)-1
        while(l<r):
            if s[l]!=s[r]:
                return False
            else:
                l+=1
                r-=1
        return True

        