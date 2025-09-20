class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        def solve(i,s):
            if len(s)==len(digits):
                res.append(s)
                return
            for c in digitToChar[digits[i]]:
                solve(i+1,s+c)
        if digits:
            solve(0,'')
        return res
        