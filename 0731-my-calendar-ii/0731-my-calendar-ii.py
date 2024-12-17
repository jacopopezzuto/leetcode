class MyCalendarTwo:

    def __init__(self):
        self.calendar=[]
        self.double_booking=[]

    def book(self, startTime: int, endTime: int) -> bool:
        for s,e in self.double_booking:
            if s<endTime and e>startTime:
                return False
        for s,e in self.calendar:
            if s<endTime and e>startTime:
                self.double_booking.append([max(s,startTime),min(e,endTime)])
        self.calendar.append([startTime,endTime])
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)