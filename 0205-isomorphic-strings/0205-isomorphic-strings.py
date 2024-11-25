class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        check=set()
        map_characters={}
        for i in range(0,len(t)):
            if s[i] in map_characters and map_characters[s[i]]!=t[i] or s[i] not in map_characters and t[i] in check:
                return False
            else:
                map_characters[s[i]]=t[i]
                check.add(t[i])
        return True