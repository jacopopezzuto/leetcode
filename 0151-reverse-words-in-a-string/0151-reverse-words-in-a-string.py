class Solution:
    def reverseWords(self, s: str) -> str:
        array_s=s.split()
        n=len(array_s)
        for i in range(0,n//2):
            array_s[i],array_s[n-i-1]=array_s[n-i-1],array_s[i]
        result=""
        for i in range(0,n):
            result+=array_s[i]
            if i!=n-1:
                result+=" "
        return result
        
            