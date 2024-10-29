class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n=len(strs)
        lcp=strs[0]
        for i in range(1,n):
            j=0
            while j<len(lcp) and j<len(strs[i]):
                if lcp[j]!=strs[i][j]:
                    break
                j+=1
            lcp=lcp[0:j]
        return lcp