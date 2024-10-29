class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        if n<2:
            return n
        l,r=0,1
        max_width=1
        occ={s[0]:1}
        curr=1
        while r<n:
            if s[r] in occ:
                while s[r] in occ:
                    del occ[s[l]]
                    curr-=1
                    l+=1
            occ[s[r]]=1
            curr+=1
            max_width=max(max_width,curr)
            r+=1
        return max_width