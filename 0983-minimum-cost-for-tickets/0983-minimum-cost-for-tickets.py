class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * 366  
        travel_days = set(days)
        
        for day in range(1,366):
            if day in travel_days:
                cost1=costs[0]+dp[day-1]
                cost7=costs[1]+dp[max(0,day-7)]
                cost30=costs[2]+dp[max(0,day-30)]
                
                dp[day] = min(cost1, cost7, cost30)
            else:
                dp[day] = dp[day - 1]
        return dp[365]