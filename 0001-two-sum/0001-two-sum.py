class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start=1
        for i,n in enumerate(nums):
            for j,m in enumerate(nums[start:]):
                if n+m == target:
                    return [i,j+start]
            start+=1
                