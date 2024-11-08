class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        map_numbers={
            '0':'0',
            '1':'1',
            '8':'8',
            '6':'9',
            '9':'6'
        }
        rotated_string=[0]*len(num)
        n=len(num)
        for i,c in enumerate(num):
            if c not in map_numbers:
                return False
            rotated_string[n-1-i]=map_numbers[c]
        return ''.join(rotated_string)==num