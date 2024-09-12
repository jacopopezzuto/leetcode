class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set=set()
        result = 0
        for i in range(len(allowed)):
            allowed_set.add(allowed[i])
        for word in words:
            find=True
            for j in word:
                if j not in allowed_set:
                    find=False
                    break
            if find == True:
                result+=1
        return result
            