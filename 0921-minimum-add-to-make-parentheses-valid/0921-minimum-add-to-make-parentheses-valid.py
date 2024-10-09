class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opened,min_adds_required=0,0
        for i in range(0,len(s)):
            if s[i] == '(':
                opened+=1
            elif s[i] == ')':
                if opened>0:
                    opened-=1
                else:
                    min_adds_required+=1
        return min_adds_required+opened
                