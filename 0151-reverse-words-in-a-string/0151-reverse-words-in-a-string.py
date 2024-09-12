class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        word = []
        i=0
        for c in s:
            if c == ' ' and len(word)>0:
                stack.append(word)
                word=[]
                i=0
            if c != ' ':
                word.insert(i,c)
                i+=1
        if len(word)>0:
            stack.append(word)
        result = ''.join(stack.pop())
        while stack:
            result=result+" "+''.join(stack.pop())
        return result
            