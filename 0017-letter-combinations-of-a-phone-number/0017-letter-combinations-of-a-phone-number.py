class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
    
        result=['']
        phone_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', 
            '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        for digit in digits:
            letters = phone_map[digit]
            temp_result=[]
            for combinations in result:
                for letter in letters:
                    temp_result.append(combinations+letter)
            result = temp_result
        return result