class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_char=""
        for i in range(len(num)-2):
                if num[i] == num[i+2] and num[i]==num[i+1]:
                    if num[i]>max_char:
                        max_char = num[i]
        return max_char*3 if max_char else ''


            
        