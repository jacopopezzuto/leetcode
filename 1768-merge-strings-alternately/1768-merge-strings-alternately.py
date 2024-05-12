class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        result = ""
        while i<len(word1) and i<len(word2):
            result+=word1[i]+word2[i]
            i+=1
        result += "" if len(word1) == len(word2) else word1[i:] if len(word1) > len(word2) else word2[i:]
        return result
            
        
            