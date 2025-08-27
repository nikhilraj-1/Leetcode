class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        row,col = len(box),len(box[0])

        for r in range(row):
            i=col-1
            for c in reversed(range(col)):
                if box[r][c]=='#': #stone
                    box[r][c],box[r][i]=box[r][i],box[r][c]
                    i-=1
                elif box[r][c]=='*': #obstacle
                    i = c-1
        res=[]
        for c in range(col):
            col =[]
            for r in reversed(range(row)):
                col.append(box[r][c])
            res.append(col)
        return res


        