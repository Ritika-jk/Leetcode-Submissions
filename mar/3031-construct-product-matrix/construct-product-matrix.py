class Solution(object):
    def constructProductMatrix(self, grid):
        m=len(grid)
        n=len(grid[0])
        lr=[] 
        for i in grid:
            for j in i:
                lr.append(j)
        rl=list(lr)
        for i in range(1,len(lr)):
            lr[i]*=lr[i-1]%12345
        for i in range(len(rl)-2,-1,-1):
            rl[i]*=rl[i+1]%12345
        for i in range(m):
            for j in range(n):
                ind=i*n+j
                if(ind==0):
                    grid[i][j]=rl[1]%12345
                elif(ind==m*n-1):
                    grid[i][j]=lr[-2]%12345
                else:
                    grid[i][j]=(lr[ind-1]*rl[ind+1])%12345
        return grid
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        