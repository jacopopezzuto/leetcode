class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n=len(strs)
        anagrams={}
        for word in strs:
            item=str(sorted(word))
            if item in anagrams:
                anagrams[item].append(word)
            else:
                anagrams[item]=[word]
        result=[]
        for item in anagrams.values():
            result.append(item)
        return result