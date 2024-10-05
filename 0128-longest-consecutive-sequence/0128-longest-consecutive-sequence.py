class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        s=set()
        result=0
        for i in range(0,n):
            s.add(nums[i])
        for i in range(0,n):
            count=0
            if nums[i]-1 not in s and nums[i] in s:
                count=0
                item_to_check = nums[i]
                while item_to_check in s:
                    count+=1
                    item_to_check+=1
                result=max(result,count)
        return result