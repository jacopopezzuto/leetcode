class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return int((high-low)/2)+1 if high%2!=0 or low%2!=0 else int((high-low)/2)