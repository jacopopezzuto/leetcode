class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        left,right=0,n-1
    
        while left!=right:
            m=(left+right)//2
            if nums[m] < nums[right]:
                right=m
            else:
                left=m+1
        return nums[left]   