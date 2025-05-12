class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for c in s:
            if c =='(' or c =='{' or c=='[':
                stack.append(c)
            else:
                if not stack:
                    return False
                elif self.matches(stack[-1],c)==False:
                    return False
                else:
                    stack.pop()

        return len(stack)==0

    def matches (self, a:str, b:str) -> bool:
        return a=='(' and b==')'or a=='{' and b=='}' or a=='[' and b==']'
            



        