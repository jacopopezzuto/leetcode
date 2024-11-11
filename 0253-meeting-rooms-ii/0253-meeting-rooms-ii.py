class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        stack=[]
        for x,y in intervals:
            stack.append([x,1])
            stack.append([y,-1])
        stack=sorted(stack)
        result=0
        calc=0
        for x,y in stack:
            calc+=y
            result=max(result,calc)
        return result