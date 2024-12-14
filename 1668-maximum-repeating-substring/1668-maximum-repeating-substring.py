class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        result = 0
        curr = word
        while curr in sequence:
            result+=1
            curr+=word
        return result