class Solution:
    def tribonacci(self, n: int) -> int:
        memo={}
        def backtracking(i:int)->int:
            if i==0:
                return 0
            if i==1 or i==2:
                return 1
            if i in memo:
                return memo[i]
            ans=backtracking(i-1)+backtracking(i-2)+backtracking(i-3)
            memo[i]=ans
            return ans
        return backtracking(n)