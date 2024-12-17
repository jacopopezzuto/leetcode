class TimeMap:

    def __init__(self):
        self.time_map={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time_map:
            self.time_map[key].append([value,timestamp])
        else:
            self.time_map[key]=[[value,timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        ans=""
        if key not in self.time_map:
            return ""
        values=self.time_map[key]
        left, right = 0, len(self.time_map[key])-1
        while left<=right:
            mid=(left+right)//2
            if values[mid][1]<=timestamp:
                ans=values[mid][0]
                left=mid+1
            else:
                right=mid-1
        return ans

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)