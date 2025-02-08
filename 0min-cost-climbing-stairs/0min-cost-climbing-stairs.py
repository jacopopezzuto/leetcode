class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo={}
        def backtracking(i:int):
            if i<0:
                return 0
            if i == 0 or i == 1:
                return cost[i]
            if i in memo:
                return memo[i]
            ans= cost[i]+min(backtracking(i-1),backtracking(i-2))
            memo[i]=ans
            return ans
        return min(backtracking(len(cost)-1),backtracking(len(cost)-2))