class Solution:
    def trap(self, height: List[int]) -> int:
        max_left=[0]*len(height)
        max_right=[0]*len(height)
        for i in range(1,len(height)):
            max_left[i]=max(height[i-1],max_left[i-1])
        for i in range(len(height)-2,-1,-1):
            max_right[i]=max(height[i+1],max_right[i+1])
        result = 0
        for i in range(1,len(height)):
            calc = min(max_left[i],max_right[i])-height[i]
            result+= 0 if calc < 0 else calc
        return result