class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict = {}
        for i in s:
            if dict.get(i) != None :
                dict[i] = dict[i]+1
            else:
                dict[i] = 1
        result = 0
        for i in dict.values():
            if i%2==0:
                result+=i
            else:
                result+=i-1
        return result+1 if result != len(s) else result