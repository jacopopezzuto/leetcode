class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        result=0
        for word in sentence.split():
            result+=1
            if len(word)<len(searchWord):
                continue
            for i in range(0,len(word)+1):
                print(word[:i],searchWord)
                if word[:i]==searchWord:
                    return result
        return -1