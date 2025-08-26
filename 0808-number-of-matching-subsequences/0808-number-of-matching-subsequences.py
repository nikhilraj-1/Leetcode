class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        hm ={}
        ans =0
        for w in words:
            hm[w]=1+hm.get(w,0)
        for w in hm:
            i=0
            j=0
            while(i<len(s) and j<len(w)):
                if s[i]==w[j]:
                    i+=1
                    j+=1
                else:
                    i+=1
            if j==len(w):
                ans+=hm[w]
        return ans
                

        