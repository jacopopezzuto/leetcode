class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        occ={}
        n=len(s)
        for c in s:
            if c in occ:
                occ[c]+=1
            else:
                occ[c]=1
        equals_to=occ[s[0]]
        for key,value in occ.items():
            if value!=equals_to:
                return False
        return True