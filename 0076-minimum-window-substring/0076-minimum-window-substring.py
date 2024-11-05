class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        dict_t={}
        for i in range(0,len(t)):
            if t[i] in dict_t:
                dict_t[t[i]]+=1
            else:
                dict_t[t[i]]=1
        
        required_length=len(dict_t)
        l=0
        formed=0
        window_counts={}
        ans= float("inf"),None,None
        
        for r in range(0,len(s)):
            character = s[r]
            if character in window_counts:
                window_counts[character]+=1
            else:
                window_counts[character]=1
            if (character in dict_t and window_counts[character]==dict_t[character]):
                formed+=1
            
            while l<=r and formed==required_length:
                character=s[l]
                if r-l+1 < ans[0]:
                    ans= (r-l+1,l,r)
                window_counts[character]-=1
                if(character in dict_t and window_counts[character]<dict_t[character]):
                    formed-=1
                l+=1
        
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]
                