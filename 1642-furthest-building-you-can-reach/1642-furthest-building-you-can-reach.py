class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        min_heap=[]
        for i in range(0,len(heights)-1):
            climb=heights[i+1]-heights[i]
            if climb<=0:
                continue
            heapq.heappush(min_heap,climb)
            if len(min_heap)<=ladders:
                continue
            bricks-=heapq.heappop(min_heap)
            if bricks < 0:
                return i
        return len(heights)-1