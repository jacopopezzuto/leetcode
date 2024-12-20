class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        result=[0]*n
        stack=[]
        for i in range(0,n):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                j=stack.pop()
                result[j]=i-j
            stack.append(i)
        return result