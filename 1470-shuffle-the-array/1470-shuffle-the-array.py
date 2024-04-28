class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i= 0
        result = []
        while i < n:
            result.append(nums[i])
            result.append(nums[i+n])
            i+=1
        return result