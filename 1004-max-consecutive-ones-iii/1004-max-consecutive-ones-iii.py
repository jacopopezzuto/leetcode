class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left,right=0,0
        n_zero=0
        result=0
        while right<len(nums):
            if nums[right]==1 or n_zero+1<=k:
                result=max(result,right-left+1)
                if nums[right]==0:
                    n_zero+=1
                right+=1
            else:
                if nums[left]==0:
                    n_zero-=1
                left+=1
        return result