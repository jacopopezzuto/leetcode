class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occ=defaultdict(int)
        for num in nums:
            occ[num]+=1
        heap=[]
        for key,value in occ.items():
            heapq.heappush(heap,(-value,key))
        result=[]
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result
            