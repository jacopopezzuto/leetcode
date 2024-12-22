class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1,y1=coordinates[0]
        x2,y2=coordinates[1]
        
        dx=x2-x1
        dy=y2-y1
        for i in range(2,len(coordinates)):
            x3,y3=coordinates[i]
            if dy*(x3-x2) != (y3-y2)*dx:
                return False
        return True