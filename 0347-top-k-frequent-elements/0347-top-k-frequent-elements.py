class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = defaultdict(dict)
        for num in nums:
            if dictionary.get(num) != None :
                dictionary.update({num : dictionary.get(num)+1})
            else :
                 dictionary.update({num : 1})
        sorted_tuples = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
        result = []
        i=0
        while i<k:
            result.append(sorted_tuples[i][0])
            i+=1
        return result
            
            