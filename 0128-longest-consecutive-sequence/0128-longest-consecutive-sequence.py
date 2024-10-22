class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        val = set(nums)
        count = 0
        for i in val:
            if (i-1) not in val:
                leng = 1
                while i+leng in val:
                    leng += 1
                count = max(count , leng)
        return count