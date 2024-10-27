class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        l,r=0,len(s)-1
        while l<r:
            while l<r and not((97<=ord(s[l])<=122) or (48<=ord(s[l])<=57)):  
                l+=1
            while l<r and not((97<=ord(s[r])<=122) or (48<=ord(s[r])<=57)):    
                r-=1
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True
        