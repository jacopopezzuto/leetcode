class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        First approach with sort
        """
        return sorted(list(s)) == sorted(list(t))
        