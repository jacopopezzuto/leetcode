class Solution:
    def makeFancyString(self, s: str) -> str:
        n=len(s)
        result=s[0]
        count=1
        for i in range(1,n):
            if s[i]==result[-1]:
                count+=1
            else:
                count=1
            if count<3:
                result+=s[i]
        return result
            
            