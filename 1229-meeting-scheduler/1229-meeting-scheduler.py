class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        timeslots=[]
        for x in slots1+slots2:
            if x[1]-x[0]>=duration:
                timeslots.append(x)
        heapq.heapify(timeslots)
        while len(timeslots)>1:
            start1, end1 = heapq.heappop(timeslots)
            start2, end2 = timeslots[0]
            if end1>= start2+duration:
                return [start2, start2+duration]
        return []