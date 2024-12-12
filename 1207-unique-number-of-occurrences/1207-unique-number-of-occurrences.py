class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        n=len(arr)
        occ = defaultdict(int)
        for item in arr:
            occ[item]+=1
        s=set()
        for key,value in occ.items():
            if value in s:
                return False
            s.add(value)
        return True