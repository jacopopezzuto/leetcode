class HitCounter:

    def __init__(self):
        self.hits=deque()

    def hit(self, timestamp: int) -> None:
        if self.hits and self.hits[-1][0]==timestamp:
            self.hits[-1]=(timestamp,self.hits[-1][1]+1)
        else:
            self.hits.append((timestamp,1))

    def getHits(self, timestamp: int) -> int:
        while self.hits and self.hits[0][0]<= timestamp-300:
            self.hits.popleft()
        result=0
        for i in range(len(self.hits)):
            result+=self.hits[i][1]
        return result
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)