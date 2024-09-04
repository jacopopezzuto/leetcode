class Solution:
    def partitionString(self, s: str) -> int:
        result = 0
        characters_set = set()
        for i in range(len(s)):
            if s[i] in characters_set:
                result +=1
                characters_set.clear()
            characters_set.add(s[i])
        return result+1 if len(characters_set)>0 else result