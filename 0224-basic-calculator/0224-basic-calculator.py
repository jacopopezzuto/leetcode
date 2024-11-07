class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        result=0
        number=0
        sign=1
        for i in range(0,len(s)):
            character=s[i]
            if character.isdigit():
                number=(number*10)+int(character)
            elif character=='(':
                stack.append(result)
                stack.append(sign)
                result=0
                sign=1
            elif character==')':
                result+=sign*number
                sign=stack.pop()
                result = stack.pop() + sign * result
                number=0
            elif character=='+':
                result+=number*sign
                number=0
                sign=1
            elif character=='-':
                result+=number*sign
                number=0
                sign=-1
        return result+(number*sign)