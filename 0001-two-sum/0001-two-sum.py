class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_nums={}
        for i,num in enumerate(nums):
            map_nums[num]=i
        for i,num in enumerate(nums):
            if target-num in map_nums and i!=map_nums[target-num]:
                return [i,map_nums[target-num]]
            