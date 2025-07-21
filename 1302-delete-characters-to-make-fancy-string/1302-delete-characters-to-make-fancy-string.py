class Solution:
    def makeFancyString(self, s: str) -> str:
        ans =[]
        res=''
        ans.append(s[0])
        prev = s[0]
        count =1
        for i in range (1,len(s)):
            if s[i]!=prev:
                count =1
                prev=s[i]
                ans.append(s[i])
            else:
                count+=1
                if(count<3):
                    ans.append(s[i])
                else:
                    continue
        res = "".join(ans)
        return res
            