class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result=[]
        n,m=len(firstList),len(secondList)
        i,j=0,0
        while i<n and j<m:
            first=max(firstList[i][0],secondList[j][0])
            second=min(firstList[i][1],secondList[j][1])
            if second >= first:
                result.append([first,second])
            if firstList[i][1] > secondList[j][1]:
                j+=1
            elif  firstList[i][1] < secondList[j][1]:
                i+=1
            else:
                j+=1
                i+=1
        return result