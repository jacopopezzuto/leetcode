class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right= 0,len(height)-1
        biggest_area=0
        while left!=right:
            #base*altezza
            area=(right-left)*min(height[left],height[right])
            biggest_area=max(biggest_area,area)
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return biggest_area