class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remaining_duration=defaultdict(int)
        result=0
        for i in range(0,len(time)):
            remainder = time[i] % 60
            item=(60-remainder)%60
            if item in remaining_duration:
                result+=remaining_duration[item]
            remaining_duration[remainder]+=1
        return result