class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        occurrences=[]
        for i in range(0,len(nums)):
            if nums[i]==x:
                occurrences.append(i)
        result=[]
        for i in range(0,len(queries)): 
            if queries[i]>len(occurrences):
                result.append(-1)
            else:
                result.append(occurrences[queries[i]-1])
        return result