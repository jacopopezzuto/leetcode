class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        Tsum = int((n * (n + 1)) / 2)
        actual_sum=0
        for item in nums:
            actual_sum+=item
        return Tsum - actual_sum