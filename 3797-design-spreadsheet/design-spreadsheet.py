class Spreadsheet:

    def __init__(self, rows: int):
        self.hm = {}
        

    def setCell(self, cell: str, value: int) -> None:
        self.hm[cell] = value

    def resetCell(self, cell: str) -> None:
        self.hm[cell]=0
        

    def getValue(self, formula: str) -> int:
        f = formula[1:]
        idx = -1
        for i in range(len(f)):
            if f[i]=='+':
                idx =i
                break
        v1,v2 = f[:i],f[i+1:]
        l =  self.hm.get(v1,0) if v1[0].isupper() else int(v1)
        r =  self.hm.get(v2,0) if v2[0].isupper() else int(v2)
        return l+r


        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)