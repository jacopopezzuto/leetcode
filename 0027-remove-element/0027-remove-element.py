class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        i,j=0,n
        while i<j:
            if nums[i]==val:
                nums[i]=None
                nums[i],nums[j-1]=nums[j-1],nums[i]
                j-=1
            else:
                i+=1
        return j