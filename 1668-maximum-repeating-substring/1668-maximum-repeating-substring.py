class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        result=0
        seq=word
        while seq in sequence:
            result+=1
            seq+=word
        return result