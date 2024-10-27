class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_nums={}
        for i in range(0,len(nums)):
            map_nums[nums[i]]=i
        for i in range(0,len(nums)):
            elem=target-nums[i]
            if elem in map_nums and map_nums[elem]!=i:
                return [map_nums[elem],i]