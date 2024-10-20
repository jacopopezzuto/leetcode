class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        left,right = 0,0
        result=float('+inf')
        curr_sum=0
        for right in range(0, n):
            curr_sum += nums[right]
            while curr_sum >= target:
                result = min(result, right - left + 1)
                curr_sum -= nums[left]
                left += 1
        return 0 if result == float(+inf) else result
                    
            
        