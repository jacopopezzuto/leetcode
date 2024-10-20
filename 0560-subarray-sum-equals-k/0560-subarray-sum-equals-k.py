class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, preSum = 0, 0
        dic, dic[0] = defaultdict(int), 1

        for num in nums:
            preSum += num
            count += dic[preSum - k]
            dic[preSum] += 1
        return count