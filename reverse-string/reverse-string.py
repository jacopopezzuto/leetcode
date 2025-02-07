class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n=len(s)
        def helper(l,r):
            if l<r:
                s[l],s[r]=s[r],s[l]
                helper(l+1,r-1)
        return helper(0,n-1)