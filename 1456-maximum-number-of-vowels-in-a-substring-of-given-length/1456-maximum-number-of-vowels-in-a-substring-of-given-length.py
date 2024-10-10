class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels={
            'a','e','i','o','u'
        }
        vowels_count=0
        for i in range(0,k):
            if s[i] in vowels:
                vowels_count+=1
        max_count=vowels_count      
        for i in range(k,len(s)):
            vowels_count+=1 if s[i] in vowels else 0
            vowels_count-=1 if s[i-k] in vowels else 0
            max_count=max(max_count,vowels_count)
        return max_count
            