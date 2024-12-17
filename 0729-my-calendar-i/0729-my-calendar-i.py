class MyCalendar:

    def __init__(self):
        self.calendar = SortedList()

    def book(self, start: int, end: int) -> bool:
        # Trova la posizione in cui l'evento potrebbe essere inserito
        idx = self.calendar.bisect_right((start, end))
        
        # Verifica se l'inserimento causa un conflitto con l'evento precedente
        if idx > 0 and self.calendar[idx-1][1] > start:
            return False
        
        # Verifica se l'inserimento causa un conflitto con l'evento successivo
        if idx < len(self.calendar) and self.calendar[idx][0] < end:
            return False
        
        # Aggiungi l'evento alla lista, mantenendo l'ordinamento
        self.calendar.add((start, end))
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)