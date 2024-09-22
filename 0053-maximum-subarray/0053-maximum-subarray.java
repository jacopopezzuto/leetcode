class Solution {
    public int maxSubArray(int[] nums) {
        int maxSum = nums[0];
        int curSum = 0;
        for(int i=0; i<nums.length; i++){
            curSum = curSum > 0 ? curSum : 0;
            curSum += nums[i];
            maxSum = maxSum > curSum ? maxSum : curSum;
        }
        return maxSum;
    }
}