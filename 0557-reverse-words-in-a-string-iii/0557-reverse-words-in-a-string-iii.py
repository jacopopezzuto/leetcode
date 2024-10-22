class Solution:
    def reverseWords(self, s: str) -> str:
        list_s=s.split()
        n=len(list_s)
        result=""
        for i in range(0,n):
            word=list_s[i]
            l,r=0,len(word)-1
            chars=list(word)
            while l<r:
                chars[l],chars[r]=chars[r],chars[l]
                l+=1
                r-=1
            new_word="".join(chars)
            result+=new_word
            if i!=n-1:
                result+=" "
        return result