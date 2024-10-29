class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq={}
        for word in words:
            if word in freq:
                freq[word]+=1
            else:
                freq[word]=1
        heap=[]
        for word,count in freq.items():
            heap.append((-count,word))
        
        heapq.heapify(heap)
        result=[]
        for i in range(0,k):
            result.append(heapq.heappop(heap)[1])
        return result
            