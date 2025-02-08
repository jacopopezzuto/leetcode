class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        map=defaultdict(int)
        max_elem=0
        for num in nums:
            map[num]+=num
            max_elem=max(max_elem,num)
        
        @cache
        def backtracking(i:int)->int:
            if i<=0:
                return 0
            if i==1:
                return map[1]
            return max(backtracking(i-1),backtracking(i-2)+map[i])
        return backtracking(max_elem)