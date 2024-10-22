class Solution:
    def reverseWords(self, s: str) -> str:
        array_s=s.split()[::-1]
        result=""
        for i in range(0,len(array_s)):
            result+=array_s[i]
            if i!=len(array_s)-1:
                result+=" "
        return result
        
            