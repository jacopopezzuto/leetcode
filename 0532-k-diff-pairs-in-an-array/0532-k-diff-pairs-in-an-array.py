class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        set_pairs=set()
        result = 0
        for i in range(len(nums)):
            j=i+1
            while j<len(nums):
                if abs(nums[i]-nums[j])==k:
                    couple = (nums[i],nums[j]) if nums[i]<nums[j] else (nums[j],nums[i])
                    if couple not in set_pairs:
                        result+=1
                        set_pairs.add(couple)
                        print(couple)
                        print(i,k)
                j+=1
        return result