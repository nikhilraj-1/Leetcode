class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        plus,minus=0,0
        for s in operations:
            if '++' in s:
                plus+=1
            else:
                minus+=1
        return plus-minus
        