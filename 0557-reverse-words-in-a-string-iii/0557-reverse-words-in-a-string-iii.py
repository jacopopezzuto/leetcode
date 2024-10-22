class Solution:
    def reverseWords(self, s: str) -> str:
        s_list=s.split()
        
        def revert(word):
            l,r=0,len(word)-1
            chars=list(word)
            while l<r:
                chars[l],chars[r]=chars[r],chars[l]
                l+=1
                r-=1
            return ''.join(chars)
        result=""
        for i in range(0,len(s_list)):
            s_list[i]=revert(s_list[i])
            result+=s_list[i]
            if i!=len(s_list)-1:
                result+=" "
            
        return result