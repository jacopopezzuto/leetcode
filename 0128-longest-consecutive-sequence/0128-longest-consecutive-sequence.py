class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set=set(nums)
        result=0
        for num in nums:
            if num-1 not in nums_set:
                curr_result=1
                while num+curr_result in nums_set:
                    curr_result+=1
                result=max(result,curr_result)
        return result