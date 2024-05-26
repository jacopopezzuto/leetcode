class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i,j = len(a)-1, len(b)-1
        c=0
        result = []
        while i>-1 or j>-1 or c:
            total = c
            if i>-1:
                total += int(a[i])
                i-=1
            if j>-1:
                total += int(b[j])
                j-=1
            result.append(str(total%2))
            c=int(total/2)
            
        return "".join(result[::-1]) 