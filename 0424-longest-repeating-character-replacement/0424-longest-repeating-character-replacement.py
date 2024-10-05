class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        char_counter = {}
        left,right = 0,0
        res=0
        max_char_counter=0
        while right<n:
            char_counter[s[right]] = char_counter.get(s[right], 0) + 1
            max_char_counter = max(char_counter[s[right]], max_char_counter)
            if (right-left+1)-max_char_counter > k:
                char_counter[s[left]]-=1
                left+=1
                
            res=max(res,right-left+1)
            right+=1
                
        return res
                