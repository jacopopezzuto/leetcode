class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dict = {}
        for c in s:
            if dict.get(c,-1) > 0:
                dict[c] = dict.get(c,-1)+1
            else:
                dict[c] = 1
        first_size = dict[s[0]]
        for item in dict:
            if first_size != dict[item]:
                return False
        return True