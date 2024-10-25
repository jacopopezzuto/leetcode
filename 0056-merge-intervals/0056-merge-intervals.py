class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)<2:
            return intervals
        intervals=sorted(intervals, key= lambda x:x[0])
        result=[intervals[0]]
        curr=1
        while curr<len(intervals):
            if result[-1][1] >= intervals[curr][0]:
                result[-1][1] = max(result[-1][1], intervals[curr][1])
            else:
                result.append(intervals[curr])
            curr+=1
        return result