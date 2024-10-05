class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result = [1]*n
        suffix=1
        for i in range(1,n):
            result[i]=nums[i-1]*result[i-1]
   
        for i in range(n-1,-1,-1):
            result[i]=suffix*result[i]
            suffix=nums[i]*suffix
        return result