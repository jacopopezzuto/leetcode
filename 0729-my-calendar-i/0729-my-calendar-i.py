class MyCalendar:

    def __init__(self):
        self.calendar = SortedList()

    def book(self, start: int, end: int) -> bool:
        # Trova la posizione corretta per il nuovo evento
        idx = self.find_insert_position(start, end)
        
        # Verifica se l'inserimento causa un conflitto con un evento esistente
        if idx > 0 and self.calendar[idx-1][1] > start:
            return False
        if idx < len(self.calendar) and self.calendar[idx][0] < end:
            return False
        
        # Aggiungi l'evento nella posizione trovata
        self.calendar.add((start, end))
        return True

    def find_insert_position(self, start: int, end: int) -> int:
        # Implementiamo manualmente la ricerca binaria per trovare la posizione corretta
        low, high = 0, len(self.calendar)
        while low < high:
            mid = (low + high) // 2
            # Confronta l'inizio dell'evento con l'inizio degli eventi nella lista
            if self.calendar[mid][0] < start:
                low = mid + 1
            else:
                high = mid
        return low
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)