class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = defaultdict(list)
        for i in range(len(nums)):
            if visited.get(target-nums[i],-1)>-1:
                return [i,visited.get(target-nums[i])]
            else:
                visited[nums[i]]=i
                