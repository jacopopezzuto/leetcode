class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i= 0
        result = []
        while i < int(len(nums)/2):
            result.extend([nums[i],nums[i+int(len(nums)/2)]])
            i+=1
        return result