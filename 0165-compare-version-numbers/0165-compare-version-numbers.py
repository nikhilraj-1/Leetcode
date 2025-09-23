class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        s1 = version1.split('.')
        s2 = version2.split('.')
        for i in range(len(s1)) :
            s1[i]=int(s1[i])
        for i in range(len(s2)) :
            s2[i]=int(s2[i])


        if len(s1)>len(s2):
            diff = len(s1)-len(s2)
            while(diff!=0):
                s2.append(int('0'))
                diff-=1
        elif len(s1)<len(s2):
            diff = len(s2)-len(s1)
            while(diff!=0):
                s1.append(int('0'))
                diff-=1

        for i,j in enumerate(range(len(s1))):
            if s1[i]<s2[j]:
                return -1
            elif s1[i]>s2[j]:
                return 1
            elif i==len(s1)-1 and j ==len(s2)-1 and s1[i]==s2[j]:
                return 0

