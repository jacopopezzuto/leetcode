class Solution:
    def calculate(self, s: str) -> int:
        curr_number=0
        operation='+'
        lastNumber=0
        operations={"+","-","*","/"}
        result=0
        for i in range(0,len(s)):
            character=s[i]
            if character!=" " and character.isdigit():
                curr_number=(curr_number*10)+int(character)
            if character in operations or i==len(s)-1:
                if operation == '-' or operation=='+':
                    result+=lastNumber
                    lastNumber=curr_number if (operation == '+') else -curr_number
                elif operation=='*':
                    lastNumber*=curr_number
                elif operation=='/':
                    if lastNumber < 0:
                        lastNumber=-(abs(lastNumber) // curr_number)
                    else:
                        lastNumber=(lastNumber // curr_number)
                operation=character
                curr_number=0
        
        result+=lastNumber
        return result