class Solution:
    def simplifyPath(self, path: str) -> str:
        '''
        "/home//foo/"
        home '' foo
        '''
        
        stack=[]
        for portion in path.split('/'):
            if not portion or portion=='.':
                continue
            elif portion=='..':
                if stack:
                    stack.pop()
            else:
                stack.append(portion)
        return '/'+'/'.join(stack)
        