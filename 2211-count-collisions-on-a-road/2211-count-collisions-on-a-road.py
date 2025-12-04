class Solution:
    def countCollisions(self, directions: str) -> int:
        leftL,rightR=0,0
        i,j=0,len(directions)-1
        countS =0
        for k in range(len(directions)):
            if directions[k] == 'S':
                countS+=1

        

        while i <len(directions) :
            if directions[i] == 'L' and (i ==0 or directions[i-1]=='L') and directions[0] == 'L':
                leftL+=1
            else:
                break
            i+=1
        while j >-1:       
            if directions[j] == 'R' and (j==len(directions)-1 or directions[j+1]=='R') and directions[len(directions)-1] == 'R':
                rightR+=1
            else:
                break
            j-=1

        return len(directions) - leftL - rightR - countS
        