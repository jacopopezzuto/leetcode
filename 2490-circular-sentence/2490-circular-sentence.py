class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words=sentence.split(" ")
        n=len(words)
        
        last=words[n-1][-1]
        for i in range(0,n):
            if last != words[i][0]:
                return False
            last=words[i][-1]
        return True