class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        max_count = 0
        result = 0
        for right in range(len(s)):
            if s[right] in count:
                count[s[right]]+=1
            else:
                count[s[right]]=1
            max_count=max(max_count,count[s[right]])
            
            if (right-left+1)-max_count>k:
                count[s[left]]-=1
                left+=1
                
            
            result=max(result,right - left + 1)
        return result
                          
                          
                          