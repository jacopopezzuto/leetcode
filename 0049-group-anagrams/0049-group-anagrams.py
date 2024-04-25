class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = defaultdict(list)

        for item in strs:
            dictionary[''.join(sorted(list(item)))].append(item)
        return dictionary.values()