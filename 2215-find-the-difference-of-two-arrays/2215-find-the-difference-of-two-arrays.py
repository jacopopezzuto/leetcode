class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1,set2=set(),set()
        for i in range(0,len(nums1)):
            set1.add(nums1[i])
        for i in range(0,len(nums2)):
            set2.add(nums2[i])
        for i in range(0,len(nums1)):
            if nums1[i] in set2:
                set2.remove(nums1[i])
        for i in range(0,len(nums2)):
            if nums2[i] in set1:
                set1.remove(nums2[i])
        return [list(set1),list(set2)]