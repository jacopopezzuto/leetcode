class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map_s, map_t = {}, {}
        for c in s:
            if c in map_s:
                map_s[c]+=1
            else:
                map_s[c]=1
        for c in t:
            if c in map_t:
                map_t[c]+=1
            else:
                map_t[c]=1
        for key, value in map_s.items():
            if key not in map_t or map_t[key]!=value:
                return False
        for key, value in map_t.items():
            if key not in map_s or map_s[key]!=value:
                return False
        return True