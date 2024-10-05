class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        left,right=0,n-1
        while left<=right:
            m=(left+right)//2
            if nums[m]==target:
                return m
            if nums[m]>=nums[left]:
                if target<nums[m] and target>=nums[left]:
                    right=m-1
                else:
                    left=m+1
            else:
                if target>nums[m] and target<=nums[right]:
                    left=m+1
                else:
                    right=m-1
                
        return -1 