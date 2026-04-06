class Solution(object):
    def robotSim(self, commands, obstacles):
        # Y+ = north 
        # x+ = east 
       directions =[( 1,0), (0,-1),(-1,0),(0,1)]
       obstacle = {tuple (obs) for obs in obstacles}
       idx , x, y ,res =3,0,0,0
       for e in commands: 
           if e == -2:
              idx = (3 +idx ) % 4

           elif e == -1: 
              idx= (1+idx ) % 4
           else :
            dx, dy = directions [idx ]
            for _ in range (e):
                nx, ny = x+dx, y+dy 
                if (nx,ny) in obstacle :
                    break 
                x,y = nx,ny
                res = max ( res , x*x+y*y)
       return res  
       