class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        stack = []

        for item in s:
            if item in brackets.keys():
                stack.append(item)
            elif len(stack)>0 and item == brackets.get(stack[-1]):
                stack.pop()
            else:
                return False
        return len(stack)==0
        