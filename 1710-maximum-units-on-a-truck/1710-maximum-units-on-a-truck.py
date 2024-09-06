class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes=sorted(boxTypes, key=lambda x: x[1])
        result=0
        j=len(boxTypes)-1
        while truckSize>0 and j>-1:
            truckSize-=1
            result+=boxTypes[j][1]
            boxTypes[j][0]-=1
            if boxTypes[j][0]==0:
                j-=1
        return result
            