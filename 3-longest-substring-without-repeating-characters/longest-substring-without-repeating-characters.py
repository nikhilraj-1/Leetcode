class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = [0]*128
        st,e,res=0,0,0
        while(e<len(s)):
            count[ord(s[e])]+=1
            while(count[ord(s[e])]>1):
                count[ord(s[st])]-=1
                st+=1
            res = max(res,e-st+1)
            e+=1
        return res
        