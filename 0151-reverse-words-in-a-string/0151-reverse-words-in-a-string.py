class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        word = ""
        i=0
        for c in s:
            if c == ' ' and len(word)>0:
                stack.append(word)
                word=""
                i=0
            if c != ' ':
                word+=c
                i+=1
        if len(word)>0:
            stack.append(word)
        return " ".join(stack[::-1])
            