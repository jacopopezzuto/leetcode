class Solution:
    def isPalindrome(self, s: str) -> bool:
        list_s = list(s.lower())
        list_s = [s for s in list_s if s.isalnum()]
        i=0
        while i<len(list_s)/2 and list_s[i] == list_s[len(list_s)-i-1]:
            i+=1
        return (i==int(len(list_s)/2)+(len(list_s)%2)) 