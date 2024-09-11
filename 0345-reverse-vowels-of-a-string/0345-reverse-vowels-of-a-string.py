class Solution:
    def reverseVowels(self, s: str) -> str:
        list_s=list(s)
        vowels = {
            'a','e','i','o','u',
            'A','E','I','O','U'
        }
        i=0
        j=len(list_s)-1
        while i<j:
            if list_s[i] in vowels and list_s[j] in vowels:
                supp=list_s[i]
                list_s[i]=list_s[j]
                list_s[j]=supp
                i+=1
                j-=1
            if list_s[i] not in vowels:
                i+=1
            if list_s[j] not in vowels:
                j-=1
        return ''.join(list_s)