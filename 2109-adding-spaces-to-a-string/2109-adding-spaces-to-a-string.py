class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        n=len(spaces)
        space_index = 0
        result=[]
        for i,c in enumerate(s):
            if space_index < n and i == spaces[space_index]:
                result.append(" ")
                space_index+=1
            result.append(c)
        return "".join(result)