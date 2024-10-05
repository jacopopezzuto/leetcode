class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        s=set()
        i,j,k = 0,1,n-1
        nums=sorted(nums)
        while i!=k and j!=k:
            calc = nums[i]+nums[j]+nums[k]
            if calc<0:
                j+=1
            elif calc>0:
                k-=1
            else:
                triplet=tuple([nums[i],nums[j],nums[k]])
                s.add(triplet)
                j+=1
            if j==k:
                i+=1
                j=i+1
                k=n-1
        return s
                        