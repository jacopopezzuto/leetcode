class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        occ1,occ2 = {},{}
        for i in s:
            if i in occ1:
                occ1[i]+=1
            else:
                occ1[i]=1
        for i in t:
            if i in occ2:
                occ2[i]+=1
            else:
                occ2[i]=1
        for key,value in occ1.items():
            if key not in occ2 or value != occ2[key]:
                return False
        return True
            
        