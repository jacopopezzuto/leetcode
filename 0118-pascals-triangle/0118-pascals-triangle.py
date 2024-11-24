class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result=[]
        for i in range(numRows):
            row=[]
            for j in range(i+1):
                row.append(None)
            row[0],row[-1]=1,1
            for j in range(1,len(row)-1):
                row[j]=result[i-1][j-1]+result[i-1][j]
            result.append(row)
        return result
            
            