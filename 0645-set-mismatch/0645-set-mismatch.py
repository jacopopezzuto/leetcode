class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = set()
        result=[-1,-1]
        for i in range(len(nums)):
            if nums[i] not in s:
                s.add(nums[i])
            else:
                result[0]=nums[i]
        for i in range(1,len(nums)+1):
            if i not in s:
                result[1]=i
                return result
            