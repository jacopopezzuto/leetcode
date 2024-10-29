class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        n=len(nums)
        for i in range(0,n):
            if nums[i] in freq:
                freq[nums[i]]+=1
            else:
                freq[nums[i]]=1
        heap=[]
        for key,value in freq.items():
            heap.append((-value,key))
        heapq.heapify(heap)
        result=[]
        for i in range(0,k):
            result.append(heapq.heappop(heap)[1])
        return result
            
            