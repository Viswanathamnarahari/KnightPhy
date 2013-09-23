'''
Created on Sep 12, 2013

@author: g7-1310us


'''
# http://stackoverflow.com/questions/6667201/how-to-define-two-dimensional-array-in-python
 




 
def nextHop(xy,r,c):
    currentRow = xy // 8
    goodRow    = currentRow + r 
    newxy      = xy + (8 * r) + c 
    newRow     = newxy // 8
    if ( (newxy < 0 ) or ( newxy > 63 ) or ( newRow != goodRow )):
        newxy = 20   
    return newxy



xy = 0
xy = 10
nxy = nextHop(xy, -2,-1); print (nxy)
nxy = nextHop(xy, -2,1) ; print (nxy)
nxy = nextHop(xy, -1,-2) ; print (nxy)
nxy = nextHop(xy, -1,2) ; print (nxy)
nxy = nextHop(xy, 1, -2) ; print (nxy)
nxy = nextHop(xy, 1, 2) ; print (nxy)
nxy = nextHop(xy, 2,-1) ; print (nxy)
nxy = nextHop(xy, 2,1) ; print (nxy)









        
    
    

