class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        left=0
        result=0
        product=1
        for right,item in enumerate(nums):
            product*=item
            while product>=k:
                product//=nums[left]
                left+=1
            result+=right-left+1
        return result
            