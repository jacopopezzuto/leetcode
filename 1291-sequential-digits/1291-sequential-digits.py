class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        potential=[]
        item=''
        for i in range(1,10):
            item=str(i)
            for j in range(i+1,10):
                item+=str(j)
                if low<=int(item)<=high: 
                    potential.append(int(item))
        return sorted(potential)
            