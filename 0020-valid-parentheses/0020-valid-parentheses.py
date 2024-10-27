class Solution:
    def isValid(self, s: str) -> bool:
        parentheses={
            '(': ')', 
            '{': '}', 
            '[': ']'
        }
        stack=[]
        for c in s:
            if c in parentheses.keys():
                stack.append(c)
            elif len(stack)>0:
                item=stack.pop()
                if c!=parentheses[item]:
                    return False
            else: 
                return False
        return False if len(stack)>0 else True 