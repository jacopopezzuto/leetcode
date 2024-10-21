class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        n=len(s)
        occ={}
        for c in s:
            if c in occ:
                occ[c]+=1
            else:
                occ[c]=1
        to_check=occ[s[0]]
        for c in s:
            if occ[c]!=to_check:
                return False
        return True