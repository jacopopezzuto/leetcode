class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        occ = defaultdict(int)
        for word in words:
            occ[word]+=1
        heap=[]
        for key,value in occ.items():
            heapq.heappush(heap,(-value,key))
        result=[]
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result