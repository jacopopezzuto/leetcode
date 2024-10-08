class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest=0
        altitudes=0
        for i in range(0,len(gain)):
            altitudes+=gain[i]
            highest=max(highest,altitudes)
        return highest