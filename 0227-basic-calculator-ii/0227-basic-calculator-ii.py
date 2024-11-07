class Solution:
    def calculate(self, s: str) -> int:
        curr_number=0
        operation='+'
        stack=[]
        operations={"+","-","*","/"}
        for i in range(0,len(s)):
            character=s[i]
            if character!=" " and character.isdigit():
                curr_number=(curr_number*10)+int(character)
            if character in operations or i==len(s)-1:
                if operation == '-':
                    stack.append(-curr_number)
                elif operation=='+':
                    stack.append(curr_number)
                elif operation=='*':
                    stack.append(stack.pop()*curr_number)
                elif operation=='/':
                    top = stack.pop()
                    if top < 0:
                        stack.append(-(abs(top) // curr_number))
                    else:
                        stack.append(top // curr_number)
                operation=character
                curr_number=0
            
        result=0
        while stack:
            result+=stack.pop()
        return result