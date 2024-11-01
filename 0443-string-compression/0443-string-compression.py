class Solution:
    def compress(self, chars: List[str]) -> int:
        i=0
        res=0
        n=len(chars)
        while i<n:
            char_counter=1
            while i+char_counter<n and chars[i]==chars[i+char_counter]:
                char_counter+=1
            if char_counter>1:
                counter=str(char_counter)
                numbers=len(counter)
                j=0
                while j<numbers:
                    chars[i+j+1]=counter[j]
                    j+=1
                while char_counter>numbers+1:
                    del chars[i+char_counter-1]
                    n-=1
                    char_counter-=1
            i+=char_counter
        
        return len(chars)