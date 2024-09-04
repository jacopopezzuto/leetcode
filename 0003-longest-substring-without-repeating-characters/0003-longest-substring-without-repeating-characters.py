class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        character_set = set()
        max_sub_length = 0
        sub_length = 0
        left=0
        for right in range(len(s)):
            while s[right] in character_set:
                character_set.remove(s[left])
                left+=1
                sub_length -=1
            character_set.add(s[right])
            sub_length +=1
            max_sub_length = (max_sub_length if max_sub_length>sub_length else sub_length )
        return max_sub_length
                
                
                
            
                