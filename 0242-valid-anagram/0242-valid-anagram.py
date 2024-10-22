class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        alphabet=[0]*26
        for i in range(0,len(s)):
            char_s=ord(s[i])-97
            char_t=ord(t[i])-97
            alphabet[char_s]+=1
            alphabet[char_t]-=1
        for i in range(0,len(alphabet)):
            if alphabet[i]!=0:
                return False
        return True
            
        