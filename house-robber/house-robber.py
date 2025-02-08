class Solution:
    def rob(self, nums: List[int]) -> int:
        memo={}
        def backtracking(i:int)->int:
            if i==0:
                return nums[0]
            if i==1:
                return max(nums[0],nums[1])
            if i in memo:
                return memo[i]
            ans= max(backtracking(i-1),nums[i]+backtracking(i-2))
            memo[i]=ans
            return ans
            
            
        return backtracking(len(nums)-1)