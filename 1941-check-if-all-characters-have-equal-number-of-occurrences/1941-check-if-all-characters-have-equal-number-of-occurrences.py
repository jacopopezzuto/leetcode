class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        occ={}
        for i in range(0,len(s)):
            if s[i] in occ:
                occ[s[i]]+=1
            else:
                occ[s[i]]=1
        to_check=occ[s[0]]
        for key,value in occ.items():
            if value!=to_check:
                return False
        return True